import sys
from os import startfile, system
from xml.dom import minidom
from listaCuadritos import listaCuadritos
from Cuadrito import Cuadrito
from Patron import Patron
from listaPatrones import listaPatrones
from Piso import Piso
from listaPisos import listaPisos
global listaPi
global nombreFabrica

#estructura de mi menu principal
def menuPrincipal():
    print("                                                                ")
    print("---------------------------Bienvenido---------------------------")
    print("|                                                              |")
    print("|************************MENU PRINCIPAL************************|")
    print("|                                                              |")
    print("|  1. Carga de archivo.                                        |")
    print("|  2. Pisos cargados.                                          |")
    print("|  0. Salir.                                                   |")
    print("----------------------------------------------------------------")

#metodo cargar archivo
def cargaarchivo():
    try:
        global listaPi
        global nombreFabrica
        documentt = minidom.parse(str(input("Ingrese la ruta de su archivo: --> ")))
        print("")
        raicita= documentt.documentElement
        nombreFabrica = raicita.nodeName#saco el nombre de la fabrica 
        listaPi = listaPisos()#creo lista de pisos
        todosLosPisos = raicita.getElementsByTagName("piso")
        for piso in todosLosPisos:
            if piso.hasAttribute("nombre"):
                nombrePiso = piso.getAttribute("nombre")
                filaTotal = piso.getElementsByTagName("R")[0]#auxiliar
                noFilas = filaTotal.childNodes[0].data
                columnaTotal = piso.getElementsByTagName("C")[0]#auxiliar
                noColumnas = columnaTotal.childNodes[0].data
                volteosTotales = piso.getElementsByTagName("F")[0]#auxiliar
                precioVolteo = volteosTotales.childNodes[0].data
                intercambiosTotales = piso.getElementsByTagName("S")[0]#auxiliar
                precioIntercambio = intercambiosTotales.childNodes[0].data

                lista_pa = listaPatrones()#lista de patrones que encuentre por piso

                patrones = piso.getElementsByTagName("patron")
                pisoUno = Piso(nombrePiso,noFilas,noColumnas,precioVolteo,precioIntercambio)#creo piso encontrado

                for patroncito in patrones:#recorro los patrones encontrados en el piso
                    if patroncito.hasAttribute("codigo"):
                        codigoPatron = patroncito.getAttribute("codigo")#codigo del patron

                        patronColores = patroncito.childNodes[0].nodeValue.split("\n")[1]#saco todo el patron
                        x=1#auxiliar
                        y=1#auxiliar
                        z=0#auxiliar
                        lista_c=listaCuadritos()#creo lista de azulejos
                        for fila in range(int(noFilas)):
                            for columna in range(int(noColumnas)):
                                cuadritoUno=Cuadrito(str(x),str(y),patronColores[z])#creo el azulejo
                                lista_c.insertarCuadrito(cuadritoUno)#meto el azulejo a la lista de azulejos
                                y=y+1
                                z=z+1
                            y=1
                            x=x+1
                        patronUno = Patron(codigoPatron)#creo patron
                        patronUno.setLista(lista_c)#meto la lista de azulejos a su patron
                        lista_pa.insertarPatron(patronUno)#meto patron a la lista de patrones
                pisoUno.setLista(lista_pa)#meto lista de patrones asu piso
                listaPi.insertarPiso(pisoUno)#meto piso a lista de pisos
        #listaPi.recorrer()
        print("El archivo se cargo con exito ✓")
    except:
        print("ocurrio un error, vuelve a intentarlo")
        print("El error fue:", sys.exc_info()[0])

#Este while me ayuda a mantener activo el menu siempre
while True:
    try:
        menuPrincipal()
        select = int(input("Selecciona alguna opción:"))
        print("\n")
        if select == 1:
            cargaarchivo()
        elif select == 2:
            listaPi.mantenerMenuPisos()
        elif select == 0:
            print("------          Gracias por usar mi programa :3           ------")
            print("----------------------------------------------------------------")
            break
        else:
            print("No existe esa opción")
    except:
        print("ocurrio un error, vuelve a intentarlo")
        print("El error fue:", sys.exc_info()[0])