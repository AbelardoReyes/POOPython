import os
from cliente import Cliente

class IntefazCliente:
    def __init__(self):
        self.llamarMetodo = Cliente()
        super().__init__()
        
    def __str__(self):
        pass
    
    def menuClientes(self):
        self.cargarJson()    
        menu = 10
        while menu != 0:
            os.system("cls")
            print("Menu de opciones")
            print("1. Agregar cliente")
            print("2. Mostrar clientes")
            print("3. Eliminar cliente")
            print("4. Modificar cliente")
            print("5. Guardar archivo")
            print("0. Salir")
            menu = int(input("Ingrese una opcion: "))
            if menu == 1:
                self.agregarCliente()
            elif menu == 2:
                self.mostarClientes()
            elif menu == 3:
                self.eliminarCliente()
            elif menu == 5:
                self.crearJson()
                
    def agregarCliente(self):
        os.system("cls")
        print("Agregar cliente")
        rfc = input("Ingrese el rfc: ")
        nombre = input("Ingrese el nombre del cliente: ")
        telefono = input("Ingrese el telefono del cliente: ")
        nuevoCLiente = Cliente(rfc, nombre, telefono)
        self.llamarMetodo.agregarEnLista(nuevoCLiente)
        print("Cliente agregado")
        enter = input("Presione enter para continuar")
    
    def mostarClientes(self):
        os.system("cls")
        print("Mostrar clientes")
        self.llamarMetodo.mostrarLista()
        enter = input("Presione enter para continuar")
        os.system("cls")
    
    def eliminarCliente(self):
        os.system("cls")
        print("Eliminar cliente")
        elemento = int(input("Ingrese el espacio de la lista que desea eliminar: "))
        if self.llamarMetodo.eliminarDeLista(elemento) == False:
            os.system("cls")
            self.eliminarCliente()
        enter = input("Presione enter para continuar")
        os.system("cls")
        
    def crearJson(self):
        lista = self.llamarMetodo.obtenerLista()
        nombreArchivo = "clientes.json"
        self.llamarMetodo.guardarArchivo(nombreArchivo, lista)
        
    def cargarJson(self):
        nombreArchivo = "clientes.json"
        diccionario = self.llamarMetodo.cargarArchivo(nombreArchivo)
        self.llamarMetodo.cargarDiccionarioALista(diccionario)
