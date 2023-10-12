
from Conexion import connect


class Persona:
    def __init__(self, idUsuario, email, password, fechaRegistro, nombre, direccion):
        self.idUsuario = idUsuario
        self.email = email
        self.password = password
        self.fechaRegistro = fechaRegistro
        self.nombre = nombre
        self.direccion = direccion
    
    
    def login():
        pass
    
    def loginOut():
        pass
    
    def verProd(self):
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM productos")
        resultado =cursor.fetchall()
        contador=1
        for prod in resultado:
            datos="{0}. IDProducto {1} | Nombre: {2} | Precio: {3}"
            print(datos.format(contador,prod[0],prod[1],prod[2],prod[3]))
            contador = contador +1
            print("")
    
    def eliminarUsuario():
        pass
    
    def registrarUsuario():
        pass
    


# aca gregue fecha registro, nombre y direccion ya que esta haciendo herencia por ende hereda lo de la clase padre
# y ademas llame a super que se utiliza para llamar a la clase base

class Usuarios(Persona):
    def __init__(self, idUsuario, email, password, fechaRegistro, nombre, direccion):
        super().__init__(idUsuario, email, password, fechaRegistro, nombre, direccion)


class Administrador(Persona):
    def __init__(self, idUsuario, email, password, fechaRegistro, nombre, direccion):
        super().__init__(idUsuario, email, password, fechaRegistro, nombre, direccion)
        self.conn, self.cursor = connect() # con esto guarda la conexión y el cursor en el objeto
        
    def cargarProd(self):
    
        
        self.nombre = input('Ingrese nombre del producto: ')
        self.descripcion = input('Ingrese la descripción del producto: ')
        self.precio = float(input('Ingrese el precio del producto: '))
        self.stock = int(input('Ingrese el stock del producto: '))
        self.idproveedor = int(input("Ingrese el id del proveedor: "))
        self.idCategoria = int(input('Ingrese la categoría del producto: '))
        

        cursor = self.conn.cursor()

        cursor.execute("INSERT INTO productos (nombre, descripcion, precio, stock, idproveedor, idCategoria) VALUES (%s, %s, %s, %s, %s, %s)", (self.nombre, self.descripcion, self.precio, self.stock, self.idproveedor, self.idCategoria))
        self.conn.commit()

        print(f"El Producto {self.nombre} se agregó exitosamente.")
            
    
    def eliminarProd():
        pass
    
    def modificarProd():
        pass






