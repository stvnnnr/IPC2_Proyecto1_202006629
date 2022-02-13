from nodoPiso import nodoPiso

class listaPisos:
    def __init__(self):
        self.cabeza = None

    def insertarPiso(self, Piso):
        if self.cabeza is None:
            self.cabeza = nodoPiso(Piso=Piso)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodoPiso(Piso=Piso)

    def recorrer(self):
        actual = self.cabeza
        while actual != None:
            listaa=actual.Piso.getLista()

            print("nombre:",actual.Piso.nombre)
            print("filas:",actual.Piso.filas)
            print("columnas:",actual.Piso.columnas)
            print("Precio volteo:",actual.Piso.volteo)
            print("Precio intercambio:",actual.Piso.intercambio)
            listaa.recorrer()
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
            actual=actual.siguiente
