from multiprocessing.reduction import send_handle
import computador
import botenook
import reloginho
import tablet

usuario = 'Lusca'
senha = 'oCar4;ehFod4Patro4!'
digital = 'Dedão'

# Instância do computador
compiuter1 = computador.desktop(marca='Postiivo',modelo='A1',cor='Preto',tamanho='Grande', usuario=usuario, senha=senha, monitor='Gamer',teclado='Logitech G512',mouse='Logitech G403',memoriaRamGB='8',placaDeVideo='GEFORCE')
compiuter1.getProcessador()
compiuter1.navegarNoChrome()


# Instância do notebook
note1 = botenook.notebook('Apple','Macbook Pro','Cinza espacial', "13.3'",usuario=usuario,senha=senha,digital=digital)
note1.ExibirEspecificacoesBasicas()
note1.getTouchPad()


# Instância do Smartwatch
relo1 = reloginho.Smartwatch('Samsung','Galaxy Watch','Preto','40 mm',usuario=usuario, senha=senha)
relo1.definirTipoDeTreino()
relo1.marcarTempoDeTreino()
relo1.mostraHorario()


# Instância do tablete
tbt = tablet.tablet('Xiaomi', 'Mi Pad 5','Branco','11"',usuario, senha,'Caneta Azul')
tbt.desenharComCaneta()
tbt.escreverComCaneta()
tbt.getMarca()