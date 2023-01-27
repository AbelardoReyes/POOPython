import os
from lista import Lista


class Producto(Lista):
    def __init__(self, codigo=None, nombre=None, descripcion=None, precio=None):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        super().__init__()

    def __str__(self):
        return f"Codigo: {self.codigo} Nombre: {self.nombre} Descripcion: {self.descripcion} Precio: {self.precio}"

    def __repr__(self):
        return f"Codigo: {self.codigo} Nombre: {self.nombre} Descripcion: {self.descripcion} Precio: {self.precio}"
    
    def cargarDiccionarioALista(self, diccionario):
        for lista in diccionario:
            producto = Producto(
                lista["codigo"], lista["nombre"], lista["descripcion"], lista["precio"])
            self.agregarEnLista(producto)
