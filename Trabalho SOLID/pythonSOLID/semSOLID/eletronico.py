import time

class Eletronicos:
    def __init__(self, marca, modelo, cor, tamanho):
        self.marca = marca
        self.cor = cor
        self.tamanho = tamanho
        self.modelo = modelo
        self.power = False

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
            power = '=('

        spec = f'''Especificações do seu eletrônico
        -------------------------------------
        Marca: {self.marca}
        Cor: {self.cor}
        Tamanho: {self.tamanho}
        Modelo: {self.modelo}
        {power}
        '''
        print(spec)

    def jogarJogoDaCobrinha(self):
        # Finge que abriu o joguinho
        for j in 'Jogo da cobrinha':
            print(j)
            time.sleep(0.5)

    def navegarNaInternet(self):
        # Você está agora acessando a interwebs
        print('Acessando a interwebs...')
        pass

    def medirBPM(self):
        # Bota no pulso e vai
        print('Relógio no pulso and go')
        time.sleep(2)

        t = 1
        for r in range(0,60):
            print(t)
            t = t+1
            time.sleep(1)

    def definirTipoDeTreino(self):
        # Esse só serve para o relógio
        pass

    def marcarTempoDeTreino(self):
        # Bota no pulso e vai treinar
        pass

    def desenharComCaneta(self):
        # serve pro tablet
        pass

    def desbloquearNaDigital(self):
        pass