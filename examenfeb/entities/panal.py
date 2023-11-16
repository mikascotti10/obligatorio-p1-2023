from entities.producto import Producto

class Panal(Producto):
    def __init__(self, codigo, nombre, marca, precio, cantidad,talle_panal,modelo_panal):
        super().__init__(codigo, nombre, marca, precio, cantidad)
        self._talle=talle_panal
        self._modelo=modelo_panal
        


