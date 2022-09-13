from itertools import product


class facturaVenta():
    def __init__(self, cliente, cuit, cantidad, precioTotal, producto):
        self.cliente=cliente
        self.cuit=cuit
        self.cantidad=cantidad
        self.precioTotal=precioTotal
        self.producto=producto

    def __str__(self):
        return """
                Nombre Cliente: {}
                CUIT Cliente: {}
                Cantidad vendida: {}
                Precio Total venta: {}
                Tipo de Producto: {}"""
factura1=facturaVenta('Irving','8888',200,300, 'Chupetines')
print(factura1.cliente,factura1.cuit,factura1.cantidad, factura1.precioTotal, factura1.producto)
        