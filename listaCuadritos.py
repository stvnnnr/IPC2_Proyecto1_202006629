from nodoCuadrito import nodoCuadrito

class listaCuadritos:
    def __init__(self):
        self.cabeza = None

    def insertarCuadrito(self, Cuadrito):
        if self.cabeza is None:
            self.cabeza = nodoCuadrito(Cuadrito=Cuadrito)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodoCuadrito(Cuadrito=Cuadrito)

    def recorrer(self):
        actual = self.cabeza
        while actual != None:
            print(" fila="+actual.Cuadrito.x,"columna="+actual.Cuadrito.y,"color:"+actual.Cuadrito.valor,"->")
            actual=actual.siguiente