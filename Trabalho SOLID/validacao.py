class ValidacaoUsuario:
    def __init__(self, usuario, senha, digital):
        self.usuario = usuario
        self.senha = senha
        self.digital = digital
        
    def entrarComDigital(self, digital):
        # Usuário faz o login com a digital inputando o dedo
        self.digital = digital
        pass

    def entrarComCredenciais(self, usuario, senha):
        # Usuário loga com login e senha
        self.usuario = usuario
        self.senha = senha
        