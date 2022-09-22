import eletronico

class tablet(eletronico.Eletronicos):
    def __init__(self, marca, modelo, cor, tamanho, ligado, caneta):
        super().__init__(marca, modelo, cor, tamanho, ligado)
        self.caneta = caneta

    def getCaneta(self):
        return self.caneta

    def setCaneta(self, caneta):
        self.caneta = caneta

    def desenharComCaneta(self):
        print('Desenhando com a caneta '+self.caneta)

    def escrevendoComCaneta(self):
        print('Escrevendo com a caneta '+self.caneta)