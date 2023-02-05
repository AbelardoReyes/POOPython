import json
import jsonpickle
from conexion import Conexion

class MyJson:
    def __init__(self):
        pass

    def guardarArchivo(self, nombreArchivo, lista):
        listaProductos = []
        for producto in lista:
            diccionario = dict(producto)
            listaProductos.append(diccionario)
            
        enter = input("Archivo guardado...")
        with open(nombreArchivo, "w") as file:
            json.dump(listaProductos, file, indent=4)

    def cargarArchivo(self, nombreArchivo):
        try:
            with open(nombreArchivo, "r") as file:
                data = json.load(file)
            return data
        except:
            return False
    

