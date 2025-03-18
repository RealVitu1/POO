class Pessoa:
    def __init__(self, nome, origem, idade, genero, cor, profissao):
        self.nome = nome
        self.origem = origem
        self.idade = idade
        self.genero = genero
        self.cor = cor
        self.profissao = profissao

    def Apresentar(self):
        return f"Me chamo {self.nome}, sou {self.profissao}, nasci em {self.origem}, tenho {self.idade} anos e minha cor é {self.cor}."
    
# exemplo de uso
pessoa = Pessoa("Victor", "Brasil", 21, "Masculino", "pardo", "engenheiro")
print(pessoa.Apresentar())