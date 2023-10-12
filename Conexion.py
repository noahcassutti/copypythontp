import mysql.connector

def connect():
    conn = mysql.connector.connect(
         host='localhost',
         database='tienda_virtual',
         user='root',
         password='#tu password'
     )
    cursor = conn.cursor()
    return conn, cursor

    


