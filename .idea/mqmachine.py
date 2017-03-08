import sqlite3

DB_NAME = 'raw_data.db'
MAIN_TABLE = 'raw_data_prozorro'

class innew():
    def __init__(self, *args, table_name = MAIN_TABLE):
        self.sqlquery = "INSERT INTO {0} VALUES {1}".format(table_name, data)
        try:
            conn = sqlite3.connect(DB_NAME)
            exquery = conn.cursor()
            exquery.execute(self.sqlquery)
            exquery.commit()
        except:
            return -1
        return 1