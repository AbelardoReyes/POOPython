import os
from producto import Producto
import pymongo
from conexion import Conexion

class InterfazProductos:
    def __init__(self):
        self.llamarMetodo = Producto()
        self.listaAlterna = Producto()
        super().__init__()

    def __str__(self) -> str:
        pass

    def menuProductos(self):
        conexion = Conexion()
        client =  conexion.iniciarConexion()
        if client != False:
            apuntador = "productos"
            database = "tienda"
            self.cargarJsonAlterno()
            diccionario = self.listaAlterna.obtenerLista()
            conexion.insertarMuchosMongo(diccionario,client,database,apuntador)
        data = self.cargarJson()
        menu = 10
        while menu != 0:
            os.system("cls")
            print("Menu de opciones")
            print("1. Agregar producto")
            print("2. Mostrar productos")
            print("3. Eliminar producto")
            print("4. Modificar producto")
            print("5. Guardar archivo")
            print("6. Traer datos de la base de datos")
            print("0. Volver al menu principal")
            menu = int(input("Ingrese una opcion: "))
            if menu == 1:
                self.agregarProducto(data)
            elif menu == 2:
                self.mostrarProductos()
            elif menu == 3:
                self.eliminarProducto()
            elif menu == 4:
                self.modificarProducto()
            elif menu == 5:
                self.crearJson()
            elif menu == 6:
                self.mostrarMongo()    


    def agregarProducto(self,data):
        os.system("cls")
        codigo = int(input("Ingrese el codigo del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripcion del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        producto = Producto(codigo, nombre, descripcion, precio)
        self.llamarMetodo.agregarEnLista(producto)
        print("Producto agregado con exito")
        diccionario = {"codigo":codigo,"nombre":nombre,"descripcion":descripcion,"precio":precio}
        input("Presione una tecla para continuar...")
        apuntador = "productos"
        conexion = Conexion()
        database = "tienda"
        client = conexion.iniciarConexion()
        if client == False:
            self.listaAlterna.agregarEnLista(producto)
            self.crearJson()
            self.crearJsonAlterno()
            print("Error al conectar con la base de datos")
            enter = input("Presione una tecla para continuar...")
        else:
            self.crearJson()
            conexion.insertarUnoMongo(diccionario,client,database,apuntador)
            enter = input("Conexion exitosa")
        os.system("cls")

    def mostrarProductos(self):
        os.system("cls")
        id = 1
        print("Lista de productos")
        # indices = ["Codigo\tNombre\tDescripcion\tPrecio"]
        self.llamarMetodo.mostrarLista(id)
        enter = input("Presione una tecla para continuar...")
        os.system("cls")

    def eliminarProducto(self):
        os.system("cls")
        elemento = int(
            input("Ingrese el espacio de la lista: "))
        if self.llamarMetodo.eliminarDeLista(elemento) == False:
            os.system("cls")
            self.eliminarProducto()
        enter = input("Presione una tecla para continuar...")
        os.system("cls")

    def modificarProducto(self):
        self.eliminarProducto()
        self.agregarProducto()

    def crearJson(self):
        lista = self.llamarMetodo.obtenerLista()
        nombreArchivo = "productos.json"
        self.llamarMetodo.guardarArchivo(nombreArchivo, lista)
            
    def crearJsonAlterno(self):
        lista = self.listaAlterna.obtenerLista()
        nombreArchivo = "productos2.json"
        self.listaAlterna.guardarArchivo(nombreArchivo, lista)

    def cargarJson(self):
        try:
            nombreArchivo = "productos.json"
            diccionario = self.llamarMetodo.cargarArchivo(nombreArchivo)
            if diccionario == False:
                self.crearJson()
            else:
                self.llamarMetodo.cargarDiccionarioALista(diccionario)
        except:
            input("No se encontro el archivo")
    
    def cargarJsonAlterno(self):
        try:
            nombreArchivo = "productos2.json"
            diccionario = self.listaAlterna.cargarArchivo(nombreArchivo)
            self.listaAlterna.cargarDiccionarioALista(diccionario)
        except:
            input("No se encontro el archivo")
        
    def mondongo(self):
        apuntador = "productos"
        conexion = Conexion()
        database = "tienda"
        client = conexion.iniciarConexion()
        conexion.mostrarMongo(client,database,apuntador)
