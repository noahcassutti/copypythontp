from Conexion import connect
from Persona import Administrador
import mysql.connector

if __name__ == '__main__':
    try:
        conn, cursor = connect() 
        print('Conexión Exitosa')
    except mysql.connector.Error as error:
        print('Conexión Fallida')
        print(error)

    mi_admi = Administrador(1, "admiss", "perrito", "2023-10-11", "admi", "mendoza")

   
    mi_admi.cargarProd() 


