from entities.producto import Producto
class Venta:
    def __init__(self,cliente,total,items):
        self._cliente=cliente
        self._total=total
        self._items=items
    @property
    def cliente(self):
        return self._cliente

    @property
    def total(self):
        return self._total

    @cliente.setter
    def cliente(self,cli):
        self._cliente=cli

    @total.setter
    def total(self,all):
        self._total=all
    
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self,itemss):
        self._items=itemss
        
    
    

        