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

    def recorrer(self):
        actual = self.cabeza
        while actual != None:
            print("------------------------------------------------")
            listadelpatron = actual.Patron.getLista()
            print(actual.Patron.codigo)
            listadelpatron.recorrer()
            actual=actual.siguiente
    
    def devuelveCabeza(self):
        actual = self.cabeza
        listaPatron = actual.Patron.getLista()
        return listaPatron

    def devuelveNombreCabeza(self):
        actual = self.cabeza
        NombrePatron = actual.Patron.codigo
        return NombrePatron