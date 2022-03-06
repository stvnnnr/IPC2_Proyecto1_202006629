from nodoPatron import nodoPatron
import sys
import os
import time
from os import startfile, system

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

    def menuPatrones(self):
        actual = self.cabeza
        print("")
        print("")
        print("")
        print("|                          MENU Patrones                          |")
        #acá iran todos los patrones del piso elegido
        n=1
        while actual != None:
            print("  ",n,".",actual.Patron.codigo,".                     ")
            n = n+1
            actual=actual.siguiente
        print("   0 . Volver .")

    def mantenerMenuPatrones(self, filas, columnas, cambio, volteo):
        correcto = False
        while (not correcto):
            self.menuPatrones()
            actual = self.cabeza
            select = int(input("selecciona alguna opción:"))
            print("\n")
            n = 1
            while actual != None:
                if select == 0:
                    correcto = True
                    break
                elif select == n:
                    self.mantenerPatronElegido(actual.Patron.codigo, filas, columnas, cambio, volteo)
                    break
                n = n+1
                actual=actual.siguiente
            if select != n and select !=0:
                print("esa opcion no existe")

    def menuPatronElegido(self, nombre):
        actual = self.cabeza
        while actual != None:
            if actual and actual.Patron.codigo == nombre:
                print("")
                print("_______________________ MENU:",actual.Patron.codigo,"_______________________")
                print("  1. Mostrar gráfica del patrón.")
                print("  2. Cambiar patrón.")
                print("  0. Volver. ")
            actual = actual.siguiente

    def mantenerPatronElegido(self, nombre, filas, columnas, cambio, volteo):
        while (True):
            try:
                self.menuPatronElegido(nombre)
                select = int(input("Selecciona alguna opción:"))
                print("\n")
                if select == 1:
                    print("Gráfica realizada")
                    self.graficar(nombre, filas, columnas)
                elif select == 2:
                    self.cambiarPatron(nombre, filas, columnas, cambio, volteo)
                elif select == 0:
                    print("volviendo...")
                    break
                else:
                    print("No existe esa opción")
            except:
                print("ocurrio un error, vuelve a intentarlo")
                print("El error fue:", sys.exc_info()[0])

    def graficar(self, nombre, filas, columnas):
        hora=time.ctime()
        actual = self.cabeza
        while actual != None:
            try:
                if actual and actual.Patron.codigo == nombre:
                    listaConPatron = actual.Patron.getLista()
                    textoConComas = listaConPatron.pintar()
                    textoSinComas = textoConComas.split(",")
                    z=0#auxiliar
                    Archivo = open('patron.dot', 'w')
                    cabeza = '''digraph structs {
                                node [shape=tripleoctagon]
                                struct3 [label=<
                                    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="2" CELLPADDING="14">
                                    <TR>
                                    <TD COLSPAN="4">'''
                    Archivo.write(cabeza)
                    Archivo.write(nombre)
                    luegoDelName = '''</TD>
                                </TR>'''
                    Archivo.write(luegoDelName)

                    for fila in range(int(filas)):
                        inicioFila = "<TR>"
                        Archivo.write(inicioFila)
                        for columna in range(int(columnas)):
                            Archivo.write(textoSinComas[z])
                            z=z+1
                        finFila = "</TR>"
                        Archivo.write(finFila)
                    finDot = '''</TABLE>>];
                            }'''
                    Archivo.write(finDot)
                    Archivo.close()
                    system('dot -Tpng patron.dot -o patron.png')
                    startfile('patron.png')
            except:
                print("ocurrio un error, vuelve a intentarlo")
                print("El error fue:", sys.exc_info()[0])
            actual = actual.siguiente

    def cambiarPatron(self, patronUno, filas, columnas, cambio, volteo):
        actual = self.cabeza
        listaUno = None
        listaDos = None
        patronDos = self.mMenuPatrones()
        while actual != None:
            if actual and actual.Patron.codigo == patronDos:
                listaDos = actual.Patron.getLista()
            actual = actual.siguiente
        textoDos = listaDos.sacarTexto()
        actual = self.cabeza
        while actual != None:
            if actual and actual.Patron.codigo == patronUno:
                listaUno = actual.Patron.getLista()
                namePatron = actual.Patron.codigo
            actual = actual.siguiente
        filas = filas.strip()
        columnas = columnas.strip()
        cambio = cambio.strip()
        volteo = volteo.strip()
        valorUno = listaUno.cambiarDos(textoDos, filas, columnas, cambio, volteo)
        print("Transformación realizada")
        instrucciones = listaUno.devolverInfo()
        instrucciones = instrucciones+"valor de la transformación fue: Q."+str(valorUno)+".00"+"\n"
        self.manMenuImpresion(instrucciones,namePatron)

    def ordenarPatrones(self):
        n = 0
        actualito = self.cabeza
        while actualito.siguiente:
            actualito = actualito.siguiente
            n = n+1
        
        for i in range(n):
            actualnova=self.cabeza
            for j in range(0, n+1):
                if actualnova.siguiente!=None and actualnova.Patron.codigo > actualnova.siguiente.Patron.codigo:
                    nodoJ = actualnova.Patron
                    nodoJ_2 = actualnova.siguiente.Patron
                    actualnova.Patron = nodoJ_2
                    actualnova.siguiente.Patron = nodoJ
                actualnova = actualnova.siguiente

    def mMenuPatrones(self):
        correcto = False
        while (not correcto):
            try:
                self.menuPatrones()
                actual = self.cabeza
                select = int(input("Por cual lo quieres cambiar?  "))
                print("\n")
                n = 1
                while actual != None:
                    if select == 0:
                        correcto = True
                        break
                    elif select == n:
                        return actual.Patron.codigo
                    n = n+1
                    actual=actual.siguiente
                if select != n and select !=0:
                    print("esa opcion no existe")
            except:
                print("ocurrio un error, vuelve a intentarlo")
                print("El error fue:", sys.exc_info()[0])

    def menuImpresion(self):
        print("")
        print("")
        print("")
        print("MENU Impresión")
        print("   1 . Consola .")
        print("   2 . Archivo de texto .")
    
    def manMenuImpresion(self, variable, namePatron):
        while True:
            try:
                self.menuImpresion()
                select = int(input("En donde deseas ver tus instrucciónes:"))
                print("\n")
                if select == 1:
                    print(variable)
                    print("\n")
                    break
                elif select == 2:
                    self.generarTxt(variable,namePatron)
                    print("Se genero archivo txt")
                    break
                else:
                    print("No existe esa opción")
            except:
                print("ocurrio un error, vuelve a intentarlo")
                print("El error fue:", sys.exc_info()[0])

    def generarTxt(self, variable, namePatron):
        nombreArchivo=namePatron+".txt"
        file = open(nombreArchivo, "w")
        file.write(variable + os.linesep)
        file.close()
        startfile(nombreArchivo)