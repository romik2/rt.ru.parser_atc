import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def create_call(conn, call):

    sql = ''' INSERT INTO call(datetime,defiant,caller_number,callee_name,called_number,first_responder,type,status,duration,incoming_line,group_data,link_to_call_recording)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, call)
    conn.commit()
    return cur.lastrowid

def end_call(conn):
    cur = conn.cursor()
    cur.execute('Select date(datetime),time(datetime),defiant,caller_number,callee_name,called_number,first_responder,type,status,duration,incoming_line,group_data,link_to_call_recording FROM call order by id desc')
    row = cur.fetchone()
    return row