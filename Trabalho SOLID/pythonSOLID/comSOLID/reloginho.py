from mimetypes import init

import eletronico
import time
import datetime


class Smartwatch(eletronico.Eletronicos):
    def __init__(self, marca, modelo, cor, tamanho, usuario, senha):
        super().__init__(marca, modelo, cor, tamanho, usuario, senha)

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
        print('Vai treinar o que hove, cria?')
        # Esse só serve para o relógio
        pass

    def marcarTempoDeTreino(self):
        print('Começando o treino em')
        i = 1
        for r in range(0,5):
            print(i)
            i = i+1
            time.sleep(1)
        print('Go!')
        # Bota no pulso e vai treinar
        pass

    def mostraHorario(self):
        agora = datetime.datetime.now()
        print('Hora:\n'+str(agora))
