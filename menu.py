class menuUso():
    def __init__(self,compra, venta, inventario):
        self.compra=compra
        self.venta= venta
        self.invetario= inventario

    def menu():
        menu = menuUso()
        while True:

            print("""
                Ingrese 1 para compra
                Ingrese 2 para venta
                Ingrese 3 para ver Inventario""")
        opcion = int(input('Elija opcion a realizar'))
        if opcion ==1:
            compra
        elif opcion ==2:
            venta 
        elif  opcion ==3:
            inventario
        elif opcion ==4:


#menu1=menuUso(1,0,10)
#print(menu1.compra, menu1.venta, menu1.invetario)
