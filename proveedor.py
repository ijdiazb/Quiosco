class Proveedor():#es en minuscula la funcion class
    def __init__(self, numero, nombre, cuit, direccion, tipoProveedor):#metodo inicialidor lleva self
        self.numero= numero
        self.nombre= nombre
        self.cuit= cuit
        self.direccion= direccion
        self.tipoProducto= tipoProveedor
    
    def __str__(self):
        return'''
            Numero Proveedor: {}
            Nombre Proveedor: {}
            CUIT Proveedor: {}
            Direccion Proveedor: {}
            Productos que vende: {}'''.format(self.numero,self.nombre, self.cuit, self.direccion, self.tipoProducto)
proveedor1=Proveedor('00001','Alfajorin', '7777', 'San Juan', 'Golosinas')
print(proveedor1.numero, proveedor1.nombre, proveedor1.cuit, proveedor1.direccion, proveedor1.tipoProducto)


        