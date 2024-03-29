from nodoCuadrito import nodoCuadrito
global letras

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
            print("fila="+actual.Cuadrito.x,"columna="+actual.Cuadrito.y,"color:"+actual.Cuadrito.valor,"->")
            actual=actual.siguiente

    def pintar(self):
        lista = "."
        actual = self.cabeza
        while actual != None:
            if actual.Cuadrito.valor == "W":
                linea = "<TD></TD>"
            else:
                linea = "<TD BGCOLOR=\"black\"></TD>"
            lista = lista +","+ linea
            actual=actual.siguiente
        lista = lista.split(".,")[1]
        return lista

    def sacarTexto(self):
        textoPlano = ""
        actual = self.cabeza
        while actual != None:
            textoPlano = textoPlano+actual.Cuadrito.valor
            actual=actual.siguiente
        return textoPlano

    def cambiarDos(self, textoDos, filas, columnas, cambio, volteo):
        global letras
        letras = ""
        actual = self.cabeza
        valor=0
        index = 0
        mov = 0
        Elemntos = 0
        nBUno=0
        nWUno=0
        actuu = actual
        actualnova = actual
        while actualnova.siguiente:
            if actualnova.Cuadrito.valor == "B":
                nBUno = nBUno+1
            elif actualnova.Cuadrito.valor == "W":
                nWUno = nWUno+1
            actualnova = actualnova.siguiente
            Elemntos = Elemntos+1
        actual=actuu


        while actual != None:
            letras = letras + "comprobando pieza no. "+ str(index+1) + " que está en la posición: " + str(actual.Cuadrito.x)+","+str(actual.Cuadrito.y)+"\n"
            actualTemp = actual
            for i in range(int(columnas)):
                if actualTemp.siguiente != None:
                    actualTemp = actualTemp.siguiente #buscamos pieza de abajo
            actualComprobacion = actual
            xElemntos = 0
            while actualComprobacion.siguiente:
                actualComprobacion = actualComprobacion.siguiente
                xElemntos = xElemntos+1

            if textoDos[index]==actual.Cuadrito.valor:#si es igual lo compueba
                letras = letras + "Pieza no. "+str(index+1)+ " es igual"+"\n"
            elif actual.siguiente == None:#Es diferente y revisa si siguiente no es None
                letras = letras + "Pieza no." + str(index+1)+" es diferente y es la ultima, la volteamos"+" costo: Q."+str(volteo)+".00"+"\n"
                actual.Cuadrito.setCuadrito(textoDos[index])#si es none, es porque es el ultimo y hace volteo
                valor = valor + int(volteo)
            elif actual.siguiente.Cuadrito.valor == textoDos[index+1]:
                actualAux = actual
                for i in range(int(columnas)):
                    if actualAux.siguiente != None:
                        actualAux = actualAux.siguiente#buscamos pieza de abajo
                if (index+int(columnas))<=Elemntos:
                    if actualAux.Cuadrito.valor == textoDos[index+int(columnas)]:
                        letras = letras + "Pieza no. "+str(index+1)+" es diferente y no se puede intercambiar, la volteamos"+" costo: Q."+str(volteo)+".00"+"\n"
                        actual.Cuadrito.setCuadrito(textoDos[index])#si es none, es porque es el ultimo y hace volteo
                        valor = valor + int(volteo)
                    elif actualAux.Cuadrito.valor != actual.Cuadrito.valor:
                        letras = letras + "Pieza no. "+str(index+1)+" es diferente y se puede intercambiar por la pieza "+ str(index+int(columnas)+1)+"\n"
                        actual.Cuadrito.setCuadrito(textoDos[index])#el de abajo es diferente tambien y lo cambiamos
                        actualNueva = actual
                        xNueva = actualAux.Cuadrito.x
                        yNueva = actualAux.Cuadrito.y
                        actual = self.cabeza
                        while actual != None:
                            if actual and actual.Cuadrito.x == xNueva:
                                if actual and actual.Cuadrito.y == yNueva:
                                    actual.Cuadrito.setCuadrito(textoDos[index+int(columnas)])
                            actual = actual.siguiente
                        actual = actualNueva
                        letras = letras + "Intercambiamos la pieza: "+actualNueva.Cuadrito.x+","+actualNueva.Cuadrito.y+" , por la pieza: "+actualAux.Cuadrito.x+","+actualAux.Cuadrito.y+" costo: Q."+str(cambio)+".00"+"\n"
                        valor = valor + int(cambio)
                    elif actualTemp.Cuadrito.valor == textoDos[index+int(columnas)]:
                        letras = letras + "Pieza no. "+str(index+1)+" es diferente y se puede intercambiar por la pieza "+str(index+2)+"\n"
                        actual.Cuadrito.setCuadrito(textoDos[index])
                        actual.siguiente.Cuadrito.setCuadrito(textoDos[index+1])
                        letras = letras + "Intercambiamos la pieza: "+actual.Cuadrito.x+","+actual.Cuadrito.y+" , por la pieza: "+actual.siguiente.Cuadrito.x+","+actual.siguiente.Cuadrito.y+" costo: Q."+str(cambio)+".00"+"\n"
                        valor = valor + int(cambio)
                else:
                    letras = letras + "Pieza no. "+str(index+1)+" es diferente y no se puede intercambiar, la volteamos"+" costo: Q."+str(volteo)+".00"+"\n"
                    actual.Cuadrito.setCuadrito(textoDos[index])#si es none, es porque es el ultimo y hace volteo
                    valor = valor + int(volteo)
            elif actual.Cuadrito.valor != actual.siguiente.Cuadrito.valor or actualTemp.Cuadrito.valor != actual.Cuadrito.valor:
                if actual.Cuadrito.valor != actual.siguiente.Cuadrito.valor:
                    letras = letras + "Pieza no. "+str(index+1)+" es diferente y se puede intercambiar por la pieza "+str(index+2)+"\n"
                    actual.Cuadrito.setCuadrito(textoDos[index])
                    actual.siguiente.Cuadrito.setCuadrito(textoDos[index+1])
                    letras = letras + "Intercambiamos la pieza: "+actual.Cuadrito.x+","+actual.Cuadrito.y+" , por la pieza: "+actual.siguiente.Cuadrito.x+","+actual.siguiente.Cuadrito.y+" costo: Q."+str(cambio)+".00"+"\n"
                    valor = valor + int(cambio)
                elif actualTemp.Cuadrito.valor != actual.Cuadrito.valor:
                    letras = letras + "Pieza no. "+str(index+1)+" es diferente y se puede intercambiar por la pieza "+str(index+int(columnas)+1)+"\n"
                    actual.Cuadrito.setCuadrito(textoDos[index])#el de abajo es diferente tambien y lo cambiamos
                    actualNueva = actual
                    xNueva = actualTemp.Cuadrito.x
                    yNueva = actualTemp.Cuadrito.y
                    actual = self.cabeza
                    while actual != None:
                        if actual and actual.Cuadrito.x == xNueva:
                            if actual and actual.Cuadrito.y == yNueva:
                                actual.Cuadrito.setCuadrito(textoDos[index+int(columnas)])
                        actual = actual.siguiente
                    actual = actualNueva
                    letras = letras + "Intercambiamos la pieza: "+actualNueva.Cuadrito.x+","+actualNueva.Cuadrito.y+" , por la pieza: "+actualTemp.Cuadrito.x+","+actualTemp.Cuadrito.y+" costo: Q."+str(cambio)+".00"+"\n"
                    valor = valor + int(cambio)
            else:
                actual.Cuadrito.setCuadrito(textoDos[index])#si es none, es porque es el ultimo y hace volteo
                letras = letras + "Pieza no. "+str(index+1)+" es diferente y no se puede intercambiar, la volteamos"+" costo: Q."+str(volteo)+".00"+"\n"
                valor = valor + int(volteo)
            letras = letras + "Pieza no. "+str(index+1)+" revisada"+"\n"
            letras = letras + "\n"
            index = index+1
            actual=actual.siguiente
        letras = letras + "\n"
        return(valor)

    def devolverInfo(self):
        global letras
        return letras