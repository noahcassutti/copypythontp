    
    
    
def cargarProd(self):
    
        cursor = self.conn.cursor()
        
        self.nombre = input('Ingrese nombre del producto: ')
        self.descripcion = input('Ingrese la descripción del producto: ')
        self.precio = input('Ingrese el precio del producto: ')
        self.stock = input('Ingrese el stock del producto: ')
        self.idCategoria = input('Ingrese la categoría del producto: ')

        sql1 = "INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s, %s)"
        val1 = (self.nombre, self.descripcion, self.precio, self.stock)
        # self.conn.execute(sql1, val1)

        
        sql2 = "INSERT INTO categoria (idCategoria) VALUES (%s)" 
        val2 = (self.idCategoria)
        # self.conn.execute(sql2, val2)
        
        self.conn.commit()

        print(f"El Producto {self.nombre} se agregó exitosamente.")
        