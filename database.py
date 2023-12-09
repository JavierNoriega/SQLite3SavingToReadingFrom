import sqlite3

global_connection = None
global_cursor = None


def create_con():
    global global_connection
    if global_connection is None:
        global_connection = sqlite3.connect('persons_DB.db')
    return global_connection


def create_cur():
    global global_cursor
    if global_cursor is None:
        global_cursor = create_con().cursor()
    return global_cursor


def sqlite_create_db():
    create_cur().execute('''
    CREATE TABLE IF NOT EXISTS personsZ(
    eyes TEXT,
    hair TEXT,
    gender TEXT
    )
    ''')

    create_con().commit()


def show_db_records(order):
    try:
        create_cur().execute(f'SELECT * FROM personsZ ORDER BY {order}')
        rows = create_cur().fetchall()

        for i in rows:
            print(i)

        create_con().close()

    except sqlite3.Error as error:
        print(f"Error showing the database: {error}")
