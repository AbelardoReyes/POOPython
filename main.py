import os
from intefazCliente import IntefazCliente
from interfazProducto import InterfazProductos
from interfazVenta import InterfazVenta
class Main:
    def __init__(self):
        pass
    def menu(self):
        os.system("cls")
        menu = 10
        while menu != 0:
            os.system('cls')
            print("Menu de opciones")
            print("1. Productos")
            print("2. Clientes")
            print("3. Ventas")
            print("0. Salir")
            menu = int(input("Ingrese una opcion: "))
            if menu == 1:
                interfazProductos = InterfazProductos()
                interfazProductos.menuProductos()
            elif menu == 2:
                interfazClientes = IntefazCliente()
                interfazClientes.menuClientes()
            elif menu == 3:
                interfazVentas = InterfazVenta()
                interfazVentas.menuVentas()
if __name__ == "__main__":
    main = Main()
    main.menu()
    print("Fin del programa")