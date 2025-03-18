class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.comChave = False

    def pegar_chave(self):
        if not self.comChave:
            self.comChave = True
            print(f"{self.nome} pegou a chave.")
        else:
            print(f"{self.nome} já tem a chave.")

    def inserir_chave(self, porta):
        if not self.comChave:
            print(f"{self.nome} deve pegar a chave primeiro.")
        elif porta.porta_open:
            print(f"{self.nome} não precisa da chave, pois a porta já está aberta.")
        else:
            porta.macaneta.ChaveIn = True
            print(f"{self.nome} inseriu a chave na porta.")

    def virar_chave(self, porta):
        if porta.macaneta.ChaveIn:
            porta.destrancada = True
            print(f"{self.nome} virou a chave, porta destrancada.")
        else:
            print(f"{self.nome} deve inserir a chave primeiro.")

    def abrir_porta(self, porta):
        if porta.destrancada:
            porta.porta_open = True
            print(f"{self.nome} abriu a porta.")
        else:
            print("Porta trancada, impossível abrir.")

    def fechar_porta(self, porta):
        if porta.porta_open:
            porta.porta_open = False
            print(f"{self.nome} fechou a porta.")
        else:
            print("A porta já está fechada.")


class Porta:
    def __init__(self, macaneta):
        self.macaneta = macaneta
        self.porta_open = False
        self.destrancada = False


class Macaneta:
    def __init__(self):
        self.ChaveIn = False


macaneta = Macaneta()
porta = Porta(macaneta)
pessoa = Pessoa("Victor")

pessoa.pegar_chave()
pessoa.inserir_chave(porta)
pessoa.virar_chave(porta)
pessoa.abrir_porta(porta)
pessoa.fechar_porta(porta)
