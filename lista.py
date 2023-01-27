import os
import pprint
from tabulate import tabulate
from myJson import MyJson


class Lista(MyJson):
    def __init__(self):
        self.lista = []

    def __str__(self):
        return {self.lista}

    def agregarEnLista(self, elemento):
        self.lista.append(elemento)

    def mostrarLista(self, apuntador):
        elementos = []
        # Para mostrar la lista de productos
        if apuntador == 1:
            cabecezera = ["codigo", "nombre", "descripcion", "precio"]
            for elemento in self.lista:
                elementos.append(
                    [elemento.codigo, elemento.nombre, elemento.descripcion, elemento.precio])
            print(tabulate(elementos, headers=cabecezera, tablefmt="fancy_grid"))
        # Para mostrar la lista de clientes
        if apuntador == 2:
            cabecezera = ["rfc", "nombre", "telefono"]
            for elemento in self.lista:
                elementos.append(
                    [elemento.rfc, elemento.nombre, elemento.telefono])
            print(tabulate(elementos, headers=cabecezera, tablefmt="fancy_grid"))

        if apuntador == 3:
            contador = 0
            cabecezera = ["cliente", "producto", "fecha", "total"]
            for elemento in self.lista:
                for producto in elemento.detalle_venta:
                    li = []
                    li.append(producto["nombre"])
                    elementos.append(
                        [elemento.cliente["nombre"], li, elemento.fecha, elemento.total])
            print(tabulate(elementos, headers=cabecezera, tablefmt="fancy_grid"))

    def eliminarDeLista(self, elemento):
        try:
            self.lista.pop(elemento)
            return True
        except:
            print("Accion fallida, no se encontro el elemento")
            enter = input("Presione una tecla para continuar...")
            return False
        enter = input("Presione una tecla para continuar...")

    def obtenerLista(self):
        li = []
        for elemento in self.lista:
            li.append(elemento.__dict__)
        return li
