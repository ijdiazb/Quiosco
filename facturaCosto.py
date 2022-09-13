class facturaCompra():
    def __init__(self, proveedorNombre, cantidad, precioTotal, producto):
        self.proveedorNombre=proveedorNombre
        self.cantidad=cantidad
        self.precioTotal=precioTotal
        self.producto=producto
    def __str__(self):
        return """
                Nombre Proveedor: {}
                Cantidad: {}
                Precio Total {}
                Tipo Producto {}""".format(self.proveedorNombre, self.cantidad, self.precioTotal, self.producto)
        
factura1=facturaCompra('Alfajorin S.A.',10,100,'alfajordulce')#isntancia un objeto
print(factura1.proveedorNombre, factura1.cantidad, factura1.precioTotal, factura1.producto)