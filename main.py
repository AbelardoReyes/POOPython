from producto import Producto
import os
from interfazProducto import InterfazProductos

class Main:
    def __init__(self):
        pass
    def menu(self):
        os.system("cls")
        menu = 10
        while menu != 0:
            print("Menu de opciones")
            print("1. Productos")
            print("0. Salir")
            menu = int(input("Ingrese una opcion: "))
            if menu == 1:
                interfazProductos = InterfazProductos()
                interfazProductos.menuProductos()

if __name__ == "__main__":
    main = Main()
    main.menu()