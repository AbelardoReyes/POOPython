import os
from lista import Lista

class Cliente(Lista):
    def __init__(self,rfc=None,nombre=None,telefono=None):
        self.rfc = rfc
        self.nombre = nombre
        self.telefono = telefono
        super().__init__()
        
    def __str__(self):
        return f"rfc: {self.rfc} nombre: {self.nombre} telefono: {self.telefono}"
    
    def __repr__(self):
        return f"rfc: {self.rfc} nombre: {self.nombre} telefono: {self.telefono}"
    
    def cargarDiccionarioALista(self, diccionario):
        for lista in diccionario:
            cliente = Cliente(
                lista["rfc"], lista["nombre"], lista["telefono"])
            self.agregarEnLista(cliente)