import sqlite3

DB_NAME = 'raw_data.db'
MAIN_TABLE = 'raw_data_prozorro'


def test_func(*args, table_name=MAIN_TABLE, db_name=DB_NAME):
    data = args[:4]
    sqlquery = "INSERT INTO {0} VALUES {1}".format(table_name, data)
    try:
        conn = sqlite3.connect(db_name)
        print("connected")
        print(sqlquery)
        exquery = conn.cursor()
        print("created cursor")
        exquery.execute(sqlquery)
        print("inserted")
        conn.commit()
        print("commited")
    except:
        raise RuntimeError

test_func(0, 0, 0, 3)