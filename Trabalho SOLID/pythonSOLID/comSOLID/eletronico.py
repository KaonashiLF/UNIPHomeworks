import time


class Eletronicos:
    def __init__(self, marca, modelo, cor, tamanho, usuario, senha):
        self.marca = marca
        self.cor = cor
        self.tamanho = tamanho
        self.modelo = modelo
        self.power = False
        self.usuario = usuario
        self.senha = senha

    #Métodos getters e setters
    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = modelo

    def getCor(self):
        return self.cor

    def setCor(self, cor):
        self.cor = cor

    def getTamanho(self):
        return self.tamanho

    def setTamanho(self, tamanho):
        self.tamanho = tamanho
    
    def getPower(self):
        return self.ligado

    def setPower(self, ligado):
        self.ligado


# -------------- Funções do A B A L O ------------------
    def Ligar(self):
        self.power = True
        self.InformaLigadoOuDesligado()

    def Desligar(self):
        self.power = False        
        self.InformaLigadoOuDesligado()

    def InformaLigadoOuDesligado(self):
        if self.power == True:
            print('O seu eletrônico está ligado!')
        else:
            print('Power Off!')

    def ExibirEspecificacoesBasicas(self):

        if self.power == True:
            power = 'Power On!'
        else:
            power = 'Power Off =('

        spec = f'''Especificações do seu eletrônico
        -------------------------------------
        Marca: {self.marca}
        Cor: {self.cor}
        Tamanho: {self.tamanho}
        Modelo: {self.modelo}
        {power}
        '''
        print(spec)
