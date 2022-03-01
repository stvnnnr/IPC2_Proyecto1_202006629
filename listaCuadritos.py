from nodoCuadrito import nodoCuadrito

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

    def cambiarUno(self, textoDos, filas, columnas, cambio, volteo):
        actual = self.cabeza
        valor=0
        index = 0
        mov = 0

        while actual != None:
            actualTemp = actual
            for i in range(int(columnas)):
                if actualTemp.siguiente != None:
                    actualTemp = actualTemp.siguiente #buscamos pieza de abajo
            if textoDos[index]==actual.Cuadrito.valor:#si es igual lo compueba
                print("pieza",actual.Cuadrito.x,actual.Cuadrito.y,"igual")
            elif actual.siguiente == None:#Es diferente y revisa si siguiente no es None
                actual.Cuadrito.setCuadrito(textoDos[index])#si es none, es porque es el ultimo y hace volteo
                mov = mov+1
                print("movimiento",mov)
                print("volteamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y)
                valor = valor + int(volteo)
            elif actual.siguiente.Cuadrito.valor == textoDos[index+1]:
                actualAux = actual
                for i in range(int(columnas)):
                    actualAux = actualAux.siguiente#buscamos pieza de abajo
                if actualAux == None:
                    actual.Cuadrito.setCuadrito(textoDos[index])#si es none, es porque es el ultimo y hace volteo
                    mov = mov+1
                    print("movimiento",mov)
                    print("volteamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y)
                    valor = valor + int(volteo)
                elif actualAux.Cuadrito.valor == textoDos[index+int(columnas)]:
                    actual.Cuadrito.setCuadrito(textoDos[index])#si es none, es porque es el ultimo y hace volteo
                    mov = mov+1
                    print("movimiento",mov)
                    print("volteamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y)
                    valor = valor + int(volteo)
                elif actualAux.Cuadrito.valor != actual.Cuadrito.valor:
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
                    mov = mov+1
                    print("movimiento",mov)
                    print("Cambiamos la pieza",actualNueva.Cuadrito.x,actualNueva.Cuadrito.y,"por la pieza",actualAux.Cuadrito.x,actualAux.Cuadrito.y)
                    valor = valor + int(cambio)
            elif actualTemp.Cuadrito.valor == textoDos[index+int(columnas)]:
                actual.Cuadrito.setCuadrito(textoDos[index])
                actual.siguiente.Cuadrito.setCuadrito(textoDos[index+1])
                mov = mov+1
                print("movimiento",mov)
                print("Cambiamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y,"por la pieza",actual.siguiente.Cuadrito.x,actual.siguiente.Cuadrito.y)
                valor = valor + int(cambio)
            elif  actualTemp.Cuadrito.valor != actual.Cuadrito.valor or actual.Cuadrito.valor != actual.siguiente.Cuadrito.valor:
                if actualTemp.Cuadrito.valor != actual.Cuadrito.valor:
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
                    mov = mov+1
                    print("movimiento",mov)
                    print("Cambiamos la pieza",actualNueva.Cuadrito.x,actualNueva.Cuadrito.y,"por la pieza",actualTemp.Cuadrito.x,actualTemp.Cuadrito.y)
                    valor = valor + int(cambio)
                elif actual.Cuadrito.valor != actual.siguiente.Cuadrito.valor:
                    actual.Cuadrito.setCuadrito(textoDos[index])
                    actual.siguiente.Cuadrito.setCuadrito(textoDos[index+1])
                    mov = mov+1
                    print("movimiento",mov)
                    print("Cambiamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y,"por la pieza",actual.siguiente.Cuadrito.x,actual.siguiente.Cuadrito.y)
                    valor = valor + int(cambio)
            print(self.sacarTexto())
            print(textoDos)
            index = index+1
            print(actual.Cuadrito.x, actual.Cuadrito.y)
            actual = actual.siguiente
        return(valor)

    def cambiarDos(self, textoDos, filas, columnas, cambio, volteo):
        actual = self.cabeza
        valor=0
        index = 0
        mov = 0

        while actual != None:
            actualTemp = actual
            for i in range(int(columnas)):
                if actualTemp.siguiente != None:
                    actualTemp = actualTemp.siguiente #buscamos pieza de abajo

            if textoDos[index]==actual.Cuadrito.valor:#si es igual lo compueba
                print("1")
                print("pieza",actual.Cuadrito.x,actual.Cuadrito.y,"igual")
            elif actual.siguiente == None:#Es diferente y revisa si siguiente no es None
                print("2")
                actual.Cuadrito.setCuadrito(textoDos[index])#si es none, es porque es el ultimo y hace volteo
                mov = mov+1
                print("movimiento",mov)
                print("volteamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y)
                valor = valor + int(volteo)
            elif actual.siguiente.Cuadrito.valor == textoDos[index+1]:
                actualAux = actual
                for i in range(int(columnas)):
                    actualAux = actualAux.siguiente#buscamos pieza de abajo
                if actualAux == None:
                    print("3")
                    actual.Cuadrito.setCuadrito(textoDos[index])#si es none, es porque es el ultimo y hace volteo
                    mov = mov+1
                    print("movimiento",mov)
                    print("volteamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y)
                    valor = valor + int(volteo)
                elif actualAux.Cuadrito.valor == textoDos[index+int(columnas)]:
                    print("4")
                    actual.Cuadrito.setCuadrito(textoDos[index])#si es none, es porque es el ultimo y hace volteo
                    mov = mov+1
                    print("movimiento",mov)
                    print("volteamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y)
                    valor = valor + int(volteo)
                elif actualAux.Cuadrito.valor != actual.Cuadrito.valor:
                    print("5")
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
                    mov = mov+1
                    print("movimiento",mov)
                    print("Cambiamos la pieza",actualNueva.Cuadrito.x,actualNueva.Cuadrito.y,"por la pieza",actualAux.Cuadrito.x,actualAux.Cuadrito.y)
                    valor = valor + int(cambio)
            elif actualTemp.Cuadrito.valor == textoDos[index+int(columnas)]:
                print("6")
                actual.Cuadrito.setCuadrito(textoDos[index])
                actual.siguiente.Cuadrito.setCuadrito(textoDos[index+1])
                mov = mov+1
                print("movimiento",mov)
                print("Cambiamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y,"por la pieza",actual.siguiente.Cuadrito.x,actual.siguiente.Cuadrito.y)
                valor = valor + int(cambio)
            elif actual.Cuadrito.valor != actual.siguiente.Cuadrito.valor or actualTemp.Cuadrito.valor != actual.Cuadrito.valor:
                if actual.Cuadrito.valor != actual.siguiente.Cuadrito.valor:
                    print("7")
                    actual.Cuadrito.setCuadrito(textoDos[index])
                    actual.siguiente.Cuadrito.setCuadrito(textoDos[index+1])
                    mov = mov+1
                    print("movimiento",mov)
                    print("Cambiamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y,"por la pieza",actual.siguiente.Cuadrito.x,actual.siguiente.Cuadrito.y)
                    valor = valor + int(cambio)
                elif actualTemp.Cuadrito.valor != actual.Cuadrito.valor:
                    print("8")
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
                    mov = mov+1
                    print("movimiento",mov)
                    print("Cambiamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y,"por la pieza",actualTemp.Cuadrito.x,actualTemp.Cuadrito.y)
                    valor = valor + int(cambio)
            else:
                actual.Cuadrito.setCuadrito(textoDos[index])#si es none, es porque es el ultimo y hace volteo
                mov = mov+1
                print("movimiento",mov)
                print("volteamos la pieza",actual.Cuadrito.x,actual.Cuadrito.y)
                valor = valor + int(volteo)
            print("Patrones luego de revisar el elemento,",index)
            print(self.sacarTexto())
            print(textoDos)
            index = index+1
            actual=actual.siguiente
        return(valor)