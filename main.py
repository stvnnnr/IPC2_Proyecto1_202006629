from xml.dom import minidom 
from xml.dom.minidom import parse
from listaCuadritos import listaCuadritos
from Cuadrito import Cuadrito
from Patron import Patron
from listaPatrones import listaPatrones
from Piso import Piso
from listaPisos import listaPisos
from tkinter import filedialog, Tk


#estructura de mi menu
def menuPrincipal():
    print("                                                                ")
    print("---------------------------Bienvenido---------------------------")
    print("|                                                              |")
    print("|************************MENU PRINCIPAL************************|")
    print("|                                                              |")
    print("|  1. Carga de archivo.                                        |")
    print("|  2. Pisos cargados.                                          |")
    print("|  3. Salir.                                                   |")
    print("----------------------------------------------------------------")

#menu de pisos
def menuPisos():
    print("                                                                ")
    print("----------------------------------------------------------------")
    print("|                                                              |")
    print("|**************************MENU PISOS**************************|")
    print("|                                                              |")
    #acá iran todos los pisos que cargue
    print("|  0. Volver.                                                   |")
    print("----------------------------------------------------------------")

#a medias aun
def mantenerMenuPisos():
    while True:
        menuPisos()
        select = int(input("selecciona alguna opción:"))
        print("\n")
        #se crearan opciones con los pisos
        if select == 1:
            print("Cargaaa")
            break
        elif select == 0:
            break

def cargaarchivo():
        documentt = minidom.parse(str(input("Ingrese la ruta de su archivo: --> ")))
        print("")
        raicita= documentt.documentElement
        nombreFabrica = raicita.nodeName
        print(nombreFabrica)
        print("-----------------------------------------------------------------")
        todosLosPisos = raicita.getElementsByTagName("piso")
        for piso in todosLosPisos:
            if piso.hasAttribute("nombre"):
                nombrePiso = piso.getAttribute("nombre")
                print("nombre:", nombrePiso)

                filaTotal = piso.getElementsByTagName("R")[0]
                noFilas = filaTotal.childNodes[0].data
                print("R:",noFilas)

                columnaTotal = piso.getElementsByTagName("C")[0]
                noColumnas = columnaTotal.childNodes[0].data
                print("C:",noColumnas)

                volteosTotales = piso.getElementsByTagName("F")[0]
                precioVolteo = volteosTotales.childNodes[0].data
                print("F:",precioVolteo)

                intercambiosTotales = piso.getElementsByTagName("S")[0]
                precioIntercambio = intercambiosTotales.childNodes[0].data
                print("S:",precioIntercambio)

                print("--------------patrones--------------")

                patrones = piso.getElementsByTagName("patron")

                for patroncito in patrones:
                    if patroncito.hasAttribute("codigo"):
                        codigoPatron = patroncito.getAttribute("codigo")
                        print("patron:", codigoPatron)

                        patronColores = patroncito.childNodes[0].nodeValue.split("\n")[1]
                        print("colores:",patronColores)




################################################################### Pruebas
# cuadritoUno = Cuadrito("1","1", "W")
# cuadritoDos = Cuadrito("2","1", "B")
# cuadritoTres = Cuadrito("3","1", "W")
# lista_e = listaCuadritos()
# lista_e.insertarCuadrito(cuadritoUno)
# lista_e.insertarCuadrito(cuadritoDos)
# lista_e.insertarCuadrito(cuadritoTres)
# lista_e.recorrer()

# patronUno = Patron("patron1",lista_e)
# lista_p = listaPatrones()
# lista_p.insertarPatron(patronUno)
# lista_p.recorrer()
#hasta aca medio sirve
#lista_p.cabeza.Patron.listaCuadritos.recorrer()

####################################################################



while True:
    cargaarchivo()






#Este while me ayuda a mantener activo el menu siempre, si sirve
# while True:
#     menuPrincipal()
#     select = int(input("Selecciona alguna opción:"))
#     print("\n")
#     if select == 1:
#         cargaarchivo()
#         print("Cargaaa")
#     elif select == 2:
#         mantenerMenuPisos()
#         print("Mostramos todos los pisos")
#     elif select == 3:
#         print("------          Gracias por usar mi programa :3           ------")
#         print("----------------------------------------------------------------")
#         break
#     else:
#         print("No existe esa opción")