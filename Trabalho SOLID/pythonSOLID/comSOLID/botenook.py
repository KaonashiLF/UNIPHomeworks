# Notebook
import eletronico

class notebook(eletronico.Eletronicos):
    def __init__(self, marca, modelo, cor, tamanho, usuario, senha, digital):
        super().__init__(marca, modelo, cor, tamanho, usuario, senha)
        self.telaLevantada = False
        self.touchpadAtivado = True
        self.digital = digital

    def getTelaLevantada(self):
        return self.telaLevantada

    def setTelaLevantada(self, levantar):
        self.telaLevantada = bool(levantar)

    def getTouchPad(self):
        if self.touchpadAtivado:
            t = 'O touchpad está ligado'
        else:
            t = 'O touchpad está desligado'
        return t

    def setTouchPad(self, touchPad):
        self.touchpadAtivado = bool(touchPad)