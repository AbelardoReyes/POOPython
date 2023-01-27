import json
import jsonpickle


class MyJson:
    def __init__(self):
        pass

    def guardarArchivo(self, nombreArchivo, lista):
        count = 0
        li = lista
        listaProductos = []
        for lista in li:
            diccionario = dict(vars(li[count]))
            listaProductos.append(diccionario)
            count += 1

        with open(nombreArchivo, "w") as file:
            json.dump(listaProductos, file, indent=4)

    def cargarArchivo(self, nombreArchivo):
        try:
            with open(nombreArchivo, "r") as file:
                data = json.load(file)
                return data
        except:
            listaProductos = []
            with open(nombreArchivo, "w") as file:
                json.dump(listaProductos, file, indent=4)
                return listaProductos
