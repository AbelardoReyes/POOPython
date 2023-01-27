import os
from lista import Lista

class Venta(Lista):
    def __init__(self,cliente=None,detalle_venta=None,fecha=None,total=None):
        self.cliente = cliente
        self.detalle_venta = detalle_venta
        self.fecha = fecha
        self.total = total
        super().__init__()
    
    def __str__(self):
        return f"Cliente: {self.cliente} Detalle de venta: {self.detalle_venta} Fecha: {self.fecha} Total: {self.total}"
    
    def __repr__(self):
        return f"Cliente: {self.cliente} Detalle de venta: {self.detalle_venta} Fecha: {self.fecha} Total: {self.total}"
    
    def cargarDiccionarioALista(self, diccionario):
        for lista in diccionario:
            venta = Venta(
                lista["cliente"], lista["detalle_venta"], lista["fecha"], lista["total"])
            self.agregarEnLista(venta)
    