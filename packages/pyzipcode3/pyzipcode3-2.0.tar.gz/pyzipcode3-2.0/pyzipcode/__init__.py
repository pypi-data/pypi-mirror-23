import time
from .settings import db_location

try:
    import sqlite3
except ImportError:
    from pysqlite2 import dbapi2 as sqlite3


class ConnectionManager(object):
    """
    Assumes a database that will work with cursor objects
    """

    def __init__(self):
        # test out the connection...
        conn = sqlite3.connect(db_location)
        conn.close()

    def query(self, sql, args=tuple()):
        conn = None
        retry_count = 0
        while not conn and retry_count <= 10:
            # If there is trouble reading the file, retry for 10 attempts then just give up...
            try:
                conn = sqlite3.connect(db_location)
            except sqlite3.OperationalError as x:
                retry_count += 1
                time.sleep(0.001)

        if not conn and retry_count > 10:
            raise sqlite3.OperationalError("Can't connect to sqlite database.")

        cursor = conn.cursor()
        cursor.execute(sql, args)
        res = cursor.fetchall()
        conn.close()
        return res


ZIP_QUERY = "SELECT * FROM zip WHERE zip_code=?"
ZIP_RANGE_QUERY = "SELECT * FROM zip WHERE longitude >= %s AND longitude <= %s AND latitude >= %s AND latitude <= %s"
ZIP_FIND_QUERY = "SELECT * FROM zip WHERE place LIKE ? AND state_code LIKE ?"


class ZipCode(object):
    def __init__(self, data):
        self.zip = data[1]
        self.place = data[2]
        self.state = data[4]
        self.latitude = data[9]
        self.longitude = data[10]


def format_result(zips):
    if len(zips) > 0:
        return [ZipCode(row) for row in zips]
    else:
        return None


class ZipNotFoundException(Exception):
    pass


class ZipCodeDatabase(object):
    def __init__(self, conn_manager=None):
        if conn_manager is None:
            conn_manager = ConnectionManager()
        self.conn_manager = conn_manager

    def get_zipcodes_around_radius(self, zip_code, radius):
        zips = self.get(zip_code)
        if zips is None:
            raise ZipNotFoundException("Could not find zip code you're searching by.")
        else:
            zip_code = zips[0]

        radius = float(radius)

        long_range = (zip_code.longitude - (radius / 69.0), zip_code.longitude + (radius / 69.0))
        lat_range = (zip_code.latitude - (radius / 49.0), zip_code.latitude + (radius / 49.0))

        return format_result(self.conn_manager.query(ZIP_RANGE_QUERY % (
            long_range[0], long_range[1],
            lat_range[0], lat_range[1]
        )))

    def find_zip(self, place=None, state=None):
        if place is None:
            place = "%"
        else:
            place = place.upper()

        if state is None:
            state = "%"
        else:
            state = state.upper()

        return format_result(self.conn_manager.query(ZIP_FIND_QUERY, (place, state)))

    def get(self, zip_code):
        return format_result(self.conn_manager.query(ZIP_QUERY, (zip_code,)))

    def __getitem__(self, zip_code):
        zip_code = self.get(str(zip_code))
        if zip_code is None:
            raise IndexError("Couldn't find ZIP")
        else:
            return zip_code[0]
