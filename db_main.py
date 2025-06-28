import sqlite3 as sql

def init_db():
    conn = sql.connect("db_library_atlas.db")
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE if not exists main_lib 
                   (isbn text(10) Primary Key,
                   title text(50),
                   author text(50),
                   genre text(20),
                   page_count text(4),
                   publish_date date,
                   publisher text(50))
''')

def ins_main_data(tuple_main_data):
    conn = sql.connect("db_library_atlas.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main_lib VALUES(?, ?, ?, ?, ?, ?, ?)", tuple_main_data)
    conn.commit()
    conn.close()
init_db()