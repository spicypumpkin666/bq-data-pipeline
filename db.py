import sqlite3
import datetime
import logging as log

from queries import INSERT

log.basicConfig(level="INFO")


class Database:

    def __init__(self, DBName):
        self.DBName = DBName
        self.__conn = self.establishConnection(self.DBName)

    def establishConnection(self, DBName):
        return sqlite3.connect(DBName)

    def execute(self, query):
        cur = self.__conn.cursor()
        cur.execute(query)

    # insert data, according to cols outlined in INSERT query. passing 'none' for ID creates auto-incrementing id in table
    def insertData(self, data):
        cur = self.__conn.cursor()
        for index in data:
            row = data[index]
            row_data = (None, row['address'], row['interactions'], row['ethBalance'], row['lastUpdatedAt'])
            cur.execute(INSERT, row_data)
            self.__conn.commit()

    # drop old data- could be configured but for our purposes here this works
    def dropOldData(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = f"DELETE FROM opensea_users WHERE lastUpdatedAt < '{now}';"
        self.execute(query)
