import sys
from os import startfile, system
from tkinter import N
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

    def ordenarPisos(self):
        n = 0
        actualito = self.cabeza
        while actualito.siguiente:
            actualito = actualito.siguiente
            n = n+1
        
        for i in range(n):
            actualnova=self.cabeza
            for j in range(0, n+1):
                if actualnova.siguiente!=None and actualnova.Piso.nombre > actualnova.siguiente.Piso.nombre:
                    nodoJ = actualnova.Piso
                    nodoJ_2 = actualnova.siguiente.Piso
                    actualnova.Piso = nodoJ_2
                    actualnova.siguiente.Piso = nodoJ
                actualnova = actualnova.siguiente

    def menuPisos(self):
        actual = self.cabeza
        print("")
        print("")
        print("")
        print("|                          MENU PISOS                          |")
        #acá iran todos los pisos que cargue
        n=1
        varOrdenUno = ""
        while actual != None:
            varOrdenUno = varOrdenUno+","+actual.Piso.nombre
            print("  ",n,".",actual.Piso.nombre,".                     ")
            n = n+1
            actual=actual.siguiente
        print("   0 . Volver .")
        # print(varOrdenUno)
        # xvar = varOrdenUno.split(",")
        # yvar = xvar.sort()
        # print(yvar)
        # sinEspacio = varOrdenUno.split(", ")
        # sinEspacio.sort()
        # print(sinEspacio)

    def mantenerMenuPisos(self):
        correcto = False
        while (not correcto):
            self.menuPisos()
            actual = self.cabeza
            select = int(input("selecciona alguna opción:"))
            print("\n")
            n = 1
            while actual != None:
                if select == 0:
                    correcto = True
                    break
                elif select == n:
                    self.mantenerpisoElegido(actual.Piso.nombre)
                    break
                n = n+1
                actual=actual.siguiente
            if select != n and select !=0:
                print("esa opcion no existe")

    def mantenerpisoElegido(self, nombre):
        while (True):
            try:
                self.menuPisoElegido(nombre)
                select = int(input("Selecciona alguna opción:"))
                print("\n")
                if select == 1:
                    self.menudePatrones(nombre)
                    #self.graficar(nombre)
                elif select == 0:
                    print("volviendo...")
                    break
                else:
                    print("No existe esa opción")
            except:
                print("ocurrio un error, vuelve a intentarlo")
                print("El error fue:", sys.exc_info()[0])

    def menuPisoElegido(self, nombre):
        actual = self.cabeza
        while actual != None:
            if actual and actual.Piso.nombre == nombre:
                print("")
                print("_______________________ MENU:",actual.Piso.nombre,"_______________________")
                print("  1. Mostrar patrones.")
                print("  0. volver.")
            actual = actual.siguiente

    def menudePatrones(self, nombre):
        actual = self.cabeza
        while actual != None:
            if actual and actual.Piso.nombre == nombre:
                filas = actual.Piso.filas
                columnas = actual.Piso.columnas
                cambio = actual.Piso.intercambio
                volteo = actual.Piso.volteo
                listaP = actual.Piso.getLista()
                listaP.mantenerMenuPatrones(filas, columnas, cambio, volteo)
            actual = actual.siguiente