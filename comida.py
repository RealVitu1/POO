class Comida:
    def __init__(self,nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.noprato = False
        self.cortada = False

    def __str__(self):
        if not self.noprato and not self.cortada:
            return f"""
            A comida {self.nome} não está no prato e nem cortada.
            """
        elif self.noprato and not self.cortada:
            return f"""
            A comida {self.nome} está no prato, mas não está cortada.
            """
        else:
            return f"""
            A comida {self.nome} está no prato e cortada.
            """
        
class Prato:
    def __init__(self, marca, tipo, tamanho):
        self.marca = marca
        self.tipo = tipo
        self.tamanho = tamanho
        self.comida = None #Declara que o atributo está vazio e pode receber o objeto comida

    def empratar(self, comida):
        self.comida = comida #Define o objeto no atributo
        if not self.comida.noprato:
            self.comida.noprato = True
            print(f"""
               A comida {self.comida.nome} está no prato {self.marca} so tipo {self.tipo}.
                  """)
        else:
            print(f"""
                A comida {self.comida.nome} já está no prato {self.marca}.
                  """)
            
class Talher:
    def __init__(self, tipo, marca, material, cor, tamanho):
        self.tipo = tipo
        self.marca = marca
        self.material = material
        self.cor = cor
        self.tamanho = tamanho

    def cortar_comida(self, comida):
        if not comida.cortada and comida.noprato:
            comida.cortada = True
            print(f"""
            A comida {comida.nome} está cortada.      
                  """)
        elif comida.cortada and comida.noprato:
            print(f"""
            A comida {comida.nome} já está cortada.      
                  """)
        else:
            print(f"""
            A comida {comida.nome} não está no prato, então não pode ser cortada.      
                  """)
            
bife = Comida("Bife", "Salgado")
prato1 = Prato("Tramontina", "Fundo", "Grande")
faca = Talher("faca", "Tramontina", "metal", "prata", "Grande")
prato1.empratar(bife)
print(bife)
