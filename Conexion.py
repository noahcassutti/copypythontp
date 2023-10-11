import mysql.connector

def connect():
    conn = mysql.connector.connect(
        host='localhost',
        database='tienda_virtual',
        user='root',
        password='#aca va la clave'
    )
    cursor = conn.cursor()
    return conn, cursor

    


