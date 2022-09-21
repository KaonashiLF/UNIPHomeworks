class Eletronicos:
    def __init__(self, marca, modelo, cor, tamanho):
        self.marca = marca
        self.cor = cor
        self.tamanho = tamanho
        self.modelo = modelo
        self.ligado = False


    def Ligar(self):
        self.ligado = True
        self.InformaLigadoOuDesligado()


    def Desligar(self):
        self.ligado = False        
        self.InformaLigadoOuDesligado()

    def InformaLigadoOuDesligado(self):
        if self.ligado == True:
            print('O seu eletrônico está ligado!')
        else:
            print('Power Off!')


    def ExibirEspecificacoesBasicas(self):

        if self.ligado == True:
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