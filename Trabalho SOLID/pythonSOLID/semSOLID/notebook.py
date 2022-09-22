import eletronico

class notebook(eletronico.Eletronicos):
    def __init__(self, marca, modelo, cor, tamanho):
        super().__init__(marca, modelo, cor, tamanho)
        self.telaLevantada = False
        self.touchpadAtivado = True

    def getTelaLevantada(self):
        return self.telaLevantada

    def setTelaLevantada(self, levantar):
        self.telaLevantada = bool(levantar)

    def getTouchPad(self):
        return self.touchpadAtivado

    def setTouchPad(self, touchPad):
        self.touchpadAtivado = bool(touchPad)

    