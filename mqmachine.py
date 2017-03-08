import sqlite3

DB_NAME = 'raw_data.db'
MAIN_TABLE = 'raw_data_prozorro'


def inNew(*args: object, table_name: object = MAIN_TABLE, db_name: object = DB_NAME, len_of_data: object = 4) -> object:
    data = args[:4]
    sqlquery = "INSERT INTO {0} VALUES {1}".format(table_name, data)
    try:
        print(data)
        print(table_name)
        conn = sqlite3.connect(db_name)
        exquery = conn.cursor()
        exquery.execute(sqlquery)
        conn.commit()
        conn.close()
    except:
        raise RuntimeError
    return "Inserted"


def delRow(*args, table_name=MAIN_TABLE, db_name=DB_NAME):
    data = args[0]
    try:
        conn = sqlite3.connect(db_name)
        exquery = conn.cursor()
        exquery.execute("pragma table_info(raw_data_prozorro)")
        column_name = exquery.fetchall()[-1][1]
        sqlquery = "DELETE FROM {0} WHERE {1}={2}".format(table_name, column_name, data)
        exquery.execute(sqlquery)
        conn.commit()
        conn.close()
    except:
        raise RuntimeError

def getChunk(*args, table_name=MAIN_TABLE, db_name=DB_NAME):
    try:
        conn = sqlite3.connect(db_name)
        exquery = conn.cursor()
        exquery.execute("pragma table_info(raw_data_prozorro)")
        column_name = exquery.fetchall()[2][1]
        sqlquery = "SELECT {0} FROM {1}".format(column_name, table_name)
        result = exquery.execute(sqlquery)
        return result
    except:
        raise RuntimeError









