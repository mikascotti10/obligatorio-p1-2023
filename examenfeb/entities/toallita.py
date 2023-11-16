from entities.producto import Producto
class Toallita(Producto):
    def __init__(self, codigo, nombre, marca, precio, cantidad):
        super().__init__(codigo, nombre, marca, precio, cantidad)
