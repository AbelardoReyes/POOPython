import os
from datetime import datetime
from cliente import Cliente
from producto import Producto
from venta import Venta
now = datetime.now()


class InterfazVenta():
    def __init__(self):
        self.listaClientes = Cliente()
        self.listaProductos = Producto()
        self.llamarMetodo = Venta()
        super().__init__()

    def menuVentas(self):
        menu = 10
        self.cargarJsonClientes()
        self.cargarJsonProductos()
        self.cargarJsonVentas()
        while menu != 0:
            os.system('cls')
            print("Menu de ventas")
            print("1. Agregar venta")
            print("2. Mostrar ventas")
            print("3. Eliminar venta")
            print("4. Modificar venta")
            print("5. Guardar archivo")
            print("0. Salir")
            menu = int(input("Ingrese una opcion: "))
            if menu == 1:
                self.agregarVenta()
            elif menu == 2:
                self.mostrarVentas()
            elif menu == 3:
                self.eliminarVenta()
            elif menu == 4:
                self.modificarVenta()
            elif menu == 5:
                self.crearJsonVentas()
                
    def modificarVenta(self):
        self.eliminarVenta()
        self.agregarVenta()
                
    def eliminarVenta(self):
        os.system("cls")
        print("Eliminar Venta")
        elemento = int(input("Ingrese el espacio de la lista que desea eliminar: "))
        if self.llamarMetodo.eliminarDeLista(elemento) == False:
            os.system("cls")
            self.eliminarVenta()
            print("Elemento eliminado")
        
    def mostrarVentas(self):
        os.system("cls")
        print("Mostrar ventas")
        self.llamarMetodo.mostrarLista()
        enter = input("Presione una tecla para continuar...")

    def agregarVenta(self):
        os.system("cls")
        print("Agregar venta")
        cliente = self.buscarCliente()
        detalle_venta = self.buscarProducto()
        #indices = ["codigo","nombre","descripcion","precio"]
        fecha = now.strftime("%d/%m/%Y")
        total = self.sumarTotal(detalle_venta)
        nuevaVenta = Venta(cliente, detalle_venta, fecha, total)
        self.llamarMetodo.agregarEnLista(nuevaVenta)
        enter = input("Presione una tecla para continuar...")
        
    def sumarTotal(self, detalle_venta):
        total = 0
        for list in detalle_venta:
            total += list.get("precio")
        return total


    def buscarCliente(self):
        os.system("cls")
        print("Buscar cliente")
        lista = self.listaClientes.obtenerLista()
        nombre = input("Ingrese el nombre del cliente: ")
        for list in lista:
            if list["nombre"] == nombre:
                print("Cliente encontrado")
                print("Nombre: ", list)
                break
        enter = input("Presione una tecla para continuar...")
        return list

    def buscarProducto(self):
        os.system("cls")
        productolist = Producto()
        op = 1
        lista = self.listaProductos.obtenerLista()
        print(lista)
        while op != 0:
            os.system("cls")
            producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            cont = 0
            for list in lista:
                if list["nombre"] == producto:
                    while cont<cantidad:
                        print("Producto encontrado")
                        producto = Producto(
                            list.get("codigo"), list.get("nombre"), list.get("descripcios"), list.get("precio"))
                        productolist.agregarEnLista(producto)
                        cont += 1
            op = int(input("Desea agregar otro producto? 1. Si 0. No: "))
        listita =  productolist.obtenerLista()
        return listita
    
    def crearJsonVentas(self):
        lista = self.llamarMetodo.obtenerLista()
        nombreArchivo = "ventas.json"
        self.llamarMetodo.guardarArchivo(nombreArchivo, lista)

    def cargarJsonClientes(self):
        nombreArchivo = "clientes.json"
        diccionario = self.listaClientes.cargarArchivo(nombreArchivo)
        self.listaClientes.cargarDiccionarioALista(diccionario)

    def cargarJsonProductos(self):
        nombreArchivo = "productos.json"
        diccionario = self.listaProductos.cargarArchivo(nombreArchivo)
        self.listaProductos.cargarDiccionarioALista(diccionario)
        
    def cargarJsonVentas(self):
        nombreArchivo = "ventas.json"
        diccionario = self.llamarMetodo.cargarArchivo(nombreArchivo)
        self.llamarMetodo.cargarDiccionarioALista(diccionario)