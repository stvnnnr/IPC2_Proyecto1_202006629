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

        while actual != None:
            letras = letras + "comprobando pieza no. "+ str(index+1) + " que está en la posición: " + str(actual.Cuadrito.x)+","+str(actual.Cuadrito.y)+"\n"
            actualTemp = actual
            for i in range(int(columnas)):
                if actualTemp.siguiente != None:
                    actualTemp = actualTemp.siguiente #buscamos pieza de abajo

            if textoDos[index]==actual.Cuadrito.valor:#si es igual lo compueba
                letras = letras + "Pieza no. "+str(index+1)+ " es igual"+"\n"
                # print("pieza",actual.Cuadrito.x,actual.Cuadrito.y,"igual")
            elif actual.siguiente == None:#Es diferente y revisa si siguiente no es None
                letras = letras + "Pieza no." + str(index+1)+" es diferente y es la ultima, la volteamos"+"\n"
                actual.Cuadrito.setCuadrito(textoDos[index])#si es none, es porque es el ultimo y hace volteo
                # mov = mov+1
                # print("movimiento",mov)
                # print("volteamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y)
                valor = valor + int(volteo)
            elif actual.siguiente.Cuadrito.valor == textoDos[index+1]:
                actualAux = actual
                for i in range(int(columnas)):
                    actualAux = actualAux.siguiente#buscamos pieza de abajo
                if actualAux == None:
                    letras = letras + "Pieza no. "+str(index+1)+" es diferente y no se puede intercambiar, la volteamos"+"\n"
                    actual.Cuadrito.setCuadrito(textoDos[index])#si es none, es porque es el ultimo y hace volteo
                    # mov = mov+1
                    # print("movimiento",mov)
                    # print("volteamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y)
                    valor = valor + int(volteo)
                elif actualAux.Cuadrito.valor == textoDos[index+int(columnas)]:
                    letras = letras + "Pieza no. "+str(index+1)+" es diferente y no se puede intercambiar, la volteamos"+"\n"
                    actual.Cuadrito.setCuadrito(textoDos[index])#si es none, es porque es el ultimo y hace volteo
                    # mov = mov+1
                    # print("movimiento",mov)
                    # print("volteamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y)
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
                    letras = letras + "Intercambiamos la pieza: "+actualNueva.Cuadrito.x+","+actualNueva.Cuadrito.y+" , por la pieza: "+actualAux.Cuadrito.x+","+actualAux.Cuadrito.y+"\n"
                    # mov = mov+1
                    # print("movimiento",mov)
                    # print("Cambiamos la pieza",actualNueva.Cuadrito.x,actualNueva.Cuadrito.y,"por la pieza",actualAux.Cuadrito.x,actualAux.Cuadrito.y)
                    valor = valor + int(cambio)
            elif actualTemp.Cuadrito.valor == textoDos[index+int(columnas)]:
                letras = letras + "Pieza no. "+str(index+1)+" es diferente y se puede intercambiar por la pieza "+str(index+2)+"\n"
                actual.Cuadrito.setCuadrito(textoDos[index])
                actual.siguiente.Cuadrito.setCuadrito(textoDos[index+1])
                letras = letras + "Intercambiamos la pieza: "+actual.Cuadrito.x+","+actual.Cuadrito.y+" , por la pieza: "+actual.siguiente.Cuadrito.x+","+actual.siguiente.Cuadrito.y+"\n"
                # mov = mov+1
                # print("movimiento",mov)
                # print("Cambiamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y,"por la pieza",actual.siguiente.Cuadrito.x,actual.siguiente.Cuadrito.y)
                valor = valor + int(cambio)
            elif actual.Cuadrito.valor != actual.siguiente.Cuadrito.valor or actualTemp.Cuadrito.valor != actual.Cuadrito.valor:
                if actual.Cuadrito.valor != actual.siguiente.Cuadrito.valor:
                    letras = letras + "Pieza no. "+str(index+1)+" es diferente y se puede intercambiar por la pieza "+str(index+2)+"\n"
                    actual.Cuadrito.setCuadrito(textoDos[index])
                    actual.siguiente.Cuadrito.setCuadrito(textoDos[index+1])
                    letras = letras + "Intercambiamos la pieza: "+actualNueva.Cuadrito.x+","+actualNueva.Cuadrito.y+" , por la pieza: "+actual.siguiente.Cuadrito.x+","+actual.siguiente.Cuadrito.y+"\n"
                    # mov = mov+1
                    # print("movimiento",mov)
                    # print("Cambiamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y,"por la pieza",actual.siguiente.Cuadrito.x,actual.siguiente.Cuadrito.y)
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
                    # mov = mov+1
                    # print("movimiento",mov)
                    # print("Cambiamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y,"por la pieza",actualTemp.Cuadrito.x,actualTemp.Cuadrito.y)
                    letras = letras + "Intercambiamos la pieza: "+actualNueva.Cuadrito.x+","+actualNueva.Cuadrito.y+" , por la pieza: "+actualTemp.Cuadrito.x+","+actualTemp.Cuadrito.y+"\n"
                    valor = valor + int(cambio)
            else:
                actual.Cuadrito.setCuadrito(textoDos[index])#si es none, es porque es el ultimo y hace volteo
                letras = letras + "Pieza no. "+str(index+1)+" es diferente y no se puede intercambiar, la volteamos"+"\n"
                # mov = mov+1
                # print("movimiento",mov)
                # print("volteamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y)
                valor = valor + int(volteo)
            # print("Patrones luego de revisar el elemento,",index)
            # print(self.sacarTexto())
            # print(textoDos)
            letras = letras + "Pieza no. "+str(index+1)+" revisada"+"\n"
            letras = letras + "\n"
            index = index+1
            actual=actual.siguiente
        letras = letras + "\n"
        return(valor)

    def devolverInfo(self):
        global letras
        return letras