import os
import pprint
from myJson import MyJson

class Lista(MyJson):
    def __init__(self):
        self.lista = []

    def __repr__(self):
        return {self.lista}

    def __str__(self):
        return {self.lista}

    def agregarEnLista(self, elemento):
        self.lista.append(elemento)

    def mostrarLista(self):
        for elemento in self.lista:
            print(elemento)
            
    def eliminarDeLista(self, elemento):
        if len(self.lista) == 0:
            print("Lista vacia")
            return True
        try:
            self.lista.pop(elemento)
        except:
            print("Accion fallida, no se encontro el elemento")
            enter = input("Presione una tecla para continuar...")
            return False
        enter = input("Presione una tecla para continuar...")
    
    def obtenerLista(self):
        return self.lista
        
            