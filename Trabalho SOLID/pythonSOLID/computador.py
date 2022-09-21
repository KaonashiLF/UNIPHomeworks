import eletronico
import platform

class desktop(eletronico.Eletronicos):
    def __init__(self, marca, modelo, cor, tamanho, monitor, teclado,mouse,memoriaRamGB, placaDeVideo):
        
        super().__init__(marca, modelo, cor, tamanho)

        self.monitor = monitor
        self.teclado = teclado
        self.mouse = mouse
        self.processador = str(platform.processor())
        self.memoriaRam = memoriaRamGB
        self.placaDeVideo = placaDeVideo


    def Processador(self):
        print('Processador: '+self.processador)


compiuter1 = desktop(marca='Postiivo',modelo='A1',cor='Preto',tamanho='Grande', monitor='Gamer',teclado='Logitech G512',mouse='Logitech G403',memoriaRamGB='8',placaDeVideo='GEFORCE')

compiuter1.Processador()