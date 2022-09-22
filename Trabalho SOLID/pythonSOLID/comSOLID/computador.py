import eletronico
import platform
import time

class desktop(eletronico.Eletronicos):
    def __init__(self, marca, modelo, cor, tamanho, usuario, senha, monitor, teclado,mouse,memoriaRamGB, placaDeVideo):
        
        super().__init__(marca, modelo, cor, tamanho, usuario, senha)

        self.monitor = monitor
        self.teclado = teclado
        self.mouse = mouse
        self.processador = str(platform.processor())
        self.memoriaRam = memoriaRamGB
        self.placaDeVideo = placaDeVideo

    def getMonitor(self):
        return self.monitor

    def setMonitor(self,monitor):
        self.monitor = monitor

    def getTeclado(self):
        return self.teclado

    def setTeclado(self, teclado):
        self.teclado = teclado

    def getMouse(self):
        return self.mouse

    def setMouse(self, mouse):
        self.mouse = mouse

    def getProcessador(self):
        return self.processador

    def setProcessador(self, processador):
        self.processador = processador

    def getRAM(self):
        ram = self.memoriaRam+' Gibas'
        return ram

    def setRAM(self, ram):
        self.memoriaRam = ram

    def getPlacaDeVideo(self):
        return self.placaDeVideo

    def setPlacaDeVideo(self, placaDeVideo):
        self.placaDeVideo = placaDeVideo

    def abrirCSGO(self):
        for r in 'Viciado':
            print(r)
            time.sleep(1)

    # 
    def navegarNoChrome(self):
        # Você está agora acessando a interwebs
        print('Acessando a interwebs...')
        pass