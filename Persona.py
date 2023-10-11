
from Conexion import connect


class Persona:
    def __init__(self, idUsuario, email, password, fechaRegistro, nombre, direccion):
        self.idUsuario = idUsuario
        self.email = email
        self.password = password
        self.fechaRegistro = fechaRegistro
        self.nombre = nombre
        self.direccion =direccion
    
    
    def login():
        pass
    
    def loginOut():
        pass
    
    def verProd():
        pass
    
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
    
        cursor = self.conn.cursor()
        self.nombre = input('Ingrese nombre del producto: ')
        self.descripcion = input('Ingrese la descripción del producto: ')
        self.precio = input('Ingrese el precio del producto: ')
        self.stock = input('Ingrese el stock del producto: ')
        self.idCategoria = input('Ingrese la categoría del producto: ')

        cursor.execute("INSERT INTO productos (nombre, descripcion, precio, stock, categoria) VALUES (%s, %s, %s, %s, %s)", (self.nombre, self.descripcion, self.precio, self.stock, self.idCategoria))
        self.conn.commit()

        print(f"El Producto {self.nombre} se agregó exitosamente.")
            
    
    def eliminarProd():
        pass
    
    def modificarProd():
        pass






