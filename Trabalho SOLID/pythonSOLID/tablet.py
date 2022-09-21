import eletronico

class tablet(eletronico.Eletronicos):
    def __init__(self, marca, modelo, cor, tamanho, ligado):
        super().__init__(marca, modelo, cor, tamanho, ligado)