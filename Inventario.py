from typing_extensions import Self


class AlmacenInventario():
    def __init__(self, producto, cantidad,precio):
        self.producto=producto
        self.cantidad=cantidad
        self.precio=precio
    
    def mostrarInventario(self):
        print('''Nombre Producto: {}
                 cantidades:{}
                 precio unitario:{}'''.format(self.producto,self.cantidad, self.precio))

    def editarInventario(self,producto, deposito,retiro):
        self.producto= producto
        self.deposito=deposito 
        self.retiro=retiro 
        self.saldo=deposito-retiro
        print ('Registro Exitoso')
    
    def mostrarHistorial(Self):
        print('Producto: {} Depositado: {} Retirado: {} Saldo: {}'.format(self.producto, self.deposito,self.reito, self.saldo))

#inventario1=AlmacenInventario('alfajor',10,100)
#print(inventario1.producto, inventario1.cantidad, inventario1.precio)
