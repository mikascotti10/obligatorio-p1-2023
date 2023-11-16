from entities.panal import Panal
from entities.producto import Producto
from entities.toallita import Toallita
from entities.venta import Venta
from exceptions.entidad_no_existe import EntidadNoExiste
from exceptions.entidad_ya_existe import EntidadYaExiste
from exceptions.informacion_invalida import InformacionInvalida

class Panalera:
    def __init__(self):
        self._productos = []
        self._ventas = []

    def es_vacio(self, dato):
        if dato == "" or dato == 0:
            return True
    def encontrar_producto(self,codigo):
        for i in self._productos:
            if i.codigo == codigo:
                return i
        return None

    def agregar_producto(self,codigo,nombre,marca,precio,cantidad,es_panal,talle_panal,modelo_panal):
            
        for p in range (len(self._productos)):
            if self._productos[p]._codigo == codigo:
                raise EntidadYaExiste()
        if self.es_vacio(es_panal):
            raise InformacionInvalida()
        if es_panal is True:
            if self.es_vacio(codigo) or self.es_vacio(nombre) or self.es_vacio(precio) or self.es_vacio(marca) or self.es_vacio(cantidad)  or self.es_vacio(talle_panal)or self.es_vacio(modelo_panal) :
                raise InformacionInvalida()
            panales=Panal(codigo, nombre, marca, precio, cantidad,talle_panal,modelo_panal)
            self._productos.append(panales)
        else:
            if self.es_vacio(codigo) or self.es_vacio(nombre) or self.es_vacio(precio) or self.es_vacio(marca) or self.es_vacio(cantidad):
                raise InformacionInvalida()
            toalla=Toallita(codigo,nombre,marca,precio,cantidad)
            self._productos.append(toalla)
    
    def	registrar_venta(self, cedula_cliente,lista_productos):

        if len(cedula_cliente) == 8 and cedula_cliente.isnumeric() and len(lista_productos) >= 1:
            precio_total = 0
            for i in range(len(lista_productos)):
                existe = False
                for v in range(len(self._productos)):
                    if lista_productos[i] == self._productos[v]._codigo:
                        precio_total += self._productos[v]._precio
                        existe = True
                if existe == False:
                    raise EntidadNoExiste()
        else:
            raise InformacionInvalida()
                    
        ventas=Venta(cedula_cliente,precio_total,lista_productos)
        self._ventas.append(ventas)
        
    def	obtener_productos_recomendados(self, cedula_cliente):

        if len(cedula_cliente) == 8 and cedula_cliente.isnumeric():
            for i in range(len(self._ventas)):
                existe = False
                if cedula_cliente == self._ventas[i]._cliente:
                    existe = True
                    cliente = i
            if existe == False:
                raise EntidadNoExiste()
            else:
                
                panales_comprados_total = []
                for i in range(len(self._ventas[cliente]._items)):
                    for v in range(len(self._productos)):
                        if self._productos[v]._codigo == self._ventas[cliente]._items[i]:
                            if type(self._productos[v]) == Panal:
                                panales_comprados_total.append(v)

                panales_comprados_no_repetidos = []
                for i in panales_comprados_total:
                    if panales_comprados_total[i] not in panales_comprados_no_repetidos:
                        panales_comprados_no_repetidos.append(panales_comprados_total[i])
                
                panales_en_venta=[]
                for i in range(len(self._productos)):
                    if type(self._productos[i]) == Panal:
                        panales_en_venta.append(i)

                panales_marca_talle = []
                for i in range(len(panales_comprados_no_repetidos)):
                    for v in range(len(panales_en_venta)):
                        if self._productos[panales_en_venta[v]]._marca != self._productos[panales_comprados_no_repetidos[i]]._marca and self._productos[panales_en_venta[v]]._talle == self._productos[panales_comprados_no_repetidos   [i]]._talle:
                            panales_marca_talle.append(self._productos[panales_en_venta[v]])

                print(panales_marca_talle)
                for i in range(len(panales_comprados_no_repetidos)):
                    print(self._productos[panales_comprados_no_repetidos[i]])
        else:
            raise InformacionInvalida()

        



            

if __name__=="__main__":
    panalera1=Panalera()
    panalera1.agregar_producto(11234,"robert","ferrari",150,1,True,"xs","hatch")
    panalera1.agregar_producto(12234,"robert","ferrari",150,1,False,"","")
    panalera1.agregar_producto(1122,"panaless","babysec",250,10,True,"l","absorvente")
    panalera1.agregar_producto(1123,"panaless","hugis",500,15,True,"l","absorvente")
    panalera1.agregar_producto(1124,"panaless","pampers",480,20,True,"l","absorvente")
    panalera1.registrar_venta("53822774",[11234,12234,1122,1123,1124])
    panalera1.obtener_productos_recomendados("53822774")
