import os
import pprint
from myJson import MyJson

class Lista(MyJson):
    def __init__(self):
        self.lista = []

    def __str__(self):
        return {self.lista}

    def agregarEnLista(self, elemento):
        self.lista.append(elemento)

    def mostrarLista(self):
        for elemento in self.lista:
            print(elemento)
            
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
        li=[]
        for elemento in self.lista:
            li.append(elemento.__dict__)
        return li
        
            