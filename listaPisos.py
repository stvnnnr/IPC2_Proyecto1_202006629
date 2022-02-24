import sys
from os import startfile, system
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

    def menuPisos(self):
        actual = self.cabeza
        print("")
        print("")
        print("")
        print("|                          MENU PISOS                          |")
        #acá iran todos los pisos que cargue
        n=1
        while actual != None:
            print("  ",n,".",actual.Piso.nombre,".                     ")
            n = n+1
            actual=actual.siguiente
        print("   0 . Volver .")

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
                    print("mostrarGrafica")
                    self.graficar(nombre)
                elif select == 2:
                    print("mostrarPatrones")
                elif select == 3:
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
                print("|_______________________ MENU:",actual.Piso.nombre,"_______________________")
                print("  1. Mostrar gráfica del patrón.")
                print("  2. Selecciónar nuevo patrón.")
                print("  3. Volver. ")
            actual = actual.siguiente

    def graficar(self, nombre):
        actual = self.cabeza
        while actual != None:
            try:
                if actual and actual.Piso.nombre == nombre:
                    listaDepatrones = actual.Piso.getLista()
                    listaConPatron = listaDepatrones.devuelveCabeza()
                    codigoPatron = listaDepatrones.devuelveNombreCabeza()
                    textoConComas = listaConPatron.pintar()
                    textoSinComas = textoConComas.split(",")
                    filas = actual.Piso.filas
                    columnas = actual.Piso.columnas
                    z=0#auxiliar

                    Archivo = open('patron.dot', 'w')
                    cabeza = '''digraph structs {
                                node [shape=tripleoctagon]
                                struct3 [label=<
                                    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="2" CELLPADDING="14">
                                    <TR>
                                    <TD COLSPAN="4">'''
                    Archivo.write(cabeza)
                    Archivo.write(codigoPatron)
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