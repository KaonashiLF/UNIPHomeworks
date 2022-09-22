import eletronico

class tablet(eletronico.Eletronicos):
    def __init__(self, marca, modelo, cor, tamanho, usuario, senha, caneta):
        super().__init__(marca, modelo, cor, tamanho, usuario, senha)
        self.caneta = caneta

    def getCaneta(self):
        return self.caneta

    def setCaneta(self, caneta):
        self.caneta = caneta

    def desenharComCaneta(self):
        print('Desenhando com a(o) '+self.caneta)

    def escreverComCaneta(self):
        print('Escrevendo com a(o) '+self.caneta)