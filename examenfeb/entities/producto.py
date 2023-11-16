from abc import ABC, abstractmethod
class Producto(ABC):
    def  __init__(self,codigo,nombre,marca,precio,cantidad):
        self._codigo=codigo
        self._nombre=nombre
        self._marca=marca
        self._precio=precio
        self._cantidad=cantidad
    
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def marca(self):
        return self._marca
    
    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad
    
    @codigo.setter
    def codnigo(self,code):
        self._codigo=code
    
    @nombre.setter
    def nombre(self,name):
        self._nombre=name
    
    @marca.setter
    def marca(self,marc):
        self._msrca=marc
    
    @precio.setter
    def precio(self,price):
        self._precio=price
    
    @cantidad.setter
    def cantidad(self,much):
        self._cantidad=much

        