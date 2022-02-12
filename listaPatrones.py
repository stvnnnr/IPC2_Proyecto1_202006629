from nodoPatron import nodoPatron

class listaPatrones:
    def __init__(self):
        self.cabeza = None

    def insertarPatron(self, Patron):
        if self.cabeza is None:
            self.cabeza = nodoPatron(Patron=Patron)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodoPatron(Patron=Patron)

    def recorrer(self):#clavosssx2
        actual = self.cabeza
        while actual != None:
            print(actual.Patron.listaCuadritos.recorrer())
            actual=actual.siguiente