import os
from producto import Producto


class InterfazProductos(Producto):
    def __init__(self):
        self.llamarMetodo = None
        super().__init__()

    def __str__(self) -> str:
        pass

    def menuProductos(self):
        self.llamarMetodo = InterfazProductos()
        menu = 10
        while menu != 0:
            os.system("cls")
            print("Menu de opciones")
            print("1. Agregar producto")
            print("2. Mostrar productos")
            print("3. Eliminar producto")
            print("4. Modificar producto")
            print("5. Guardar archivo")
            print("0. Volver al menu principal")
            menu = int(input("Ingrese una opcion: "))
            if menu == 1:
                self.agregarProducto()
            elif menu == 2:
                self.mostrarProductos()
            elif menu == 3:
                self.eliminarProducto()
            elif menu == 4:
                self.modificarProducto()
            elif menu == 5:
                self.crearJson()

    def agregarProducto(self, id=0):
        os.system("cls")
        codigo = int(input("Ingrese el codigo del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripcion del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        producto = Producto(codigo, nombre, descripcion, precio)
        self.llamarMetodo.agregarEnLista(producto)
        print("Producto agregado con exito")
        input("Presione una tecla para continuar...")
        os.system("cls")

    def mostrarProductos(self):
        os.system("cls")
        print("Lista de productos")
        # indices = ["Codigo\tNombre\tDescripcion\tPrecio"]
        self.llamarMetodo.mostrarLista()
        enter = input("Presione una tecla para continuar...")
        os.system("cls")

    def eliminarProducto(self):
        os.system("cls")
        elemento = int(
            input("Ingrese el espacio de la lista que desea eliminar:"))
        if self.llamarMetodo.eliminarDeLista(elemento) == False:
            os.system("cls")
            self.eliminarProducto()
        enter = input("Presione una tecla para continuar...")
        os.system("cls")

    def modificarProducto(self):
        self.llamarMetodo.eliminarProducto()
        self.llamarMetodo.agregarProducto(id)
        
    def crearJson(self):
        lista = self.llamarMetodo.obtenerLista()
        nombreArchivo = "productos.json"    
        self.llamarMetodo.guardarArchivo(nombreArchivo, lista)
