from listaCuadritos import listaCuadritos
class Patron:
    def __init__(self, codigo):
        self.codigo = codigo
        self.listaCuadritos = listaCuadritos
    
    def setLista(self, listaCuadritos):
        self.listaCuadritos = listaCuadritos

    def getLista(self):
        return self.listaCuadritos