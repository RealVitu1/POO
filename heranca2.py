class Automovel:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.marca} ligado.")
        else:
            print(f"{self.marca} já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"{self.marca} desligado.")
        else:
            print(f"{self.marca} não está ligado, ligue-o antes.")

    def passar_marcha(self):
        if self.ligado:
            print(f"{self.marca} passou de marcha.")
        else:
            print(f"{self.marca} está desligado, impossível passar de marcha.")

class Carro(Automovel):
    def __init__(self, marca, ano, potencia, num_marcha):
        super().__init__(marca, ano)
        self.potencia = potencia
        self.num_marcha = num_marcha

    def acelerar(self):
        if self.ligado:
            print(f"{self.marca} está acelerando.")
        else:
            print(f"{self.marca} não está ligado, precisa estar ligado para acelerar.")

class Moto(Automovel):
    def __init__(self, marca, ano, cilindrada, num_marcha):
        super().__init__(marca, ano)
        self.cilindrada = cilindrada
        self.num_marcha = num_marcha

    def acelerar(self):
        if self.ligado:
            print(f"{self.marca} está acelerando.")
        else:
            print(f"{self.marca} não está ligado, precisa estar ligado para acelerar.")

class Motorista:
    def __init__(self, habilitacao):
        self.habilitacao = habilitacao

    def subir_moto(self, moto):
        if "A" in self.habilitacao or "a" in self.habilitacao:
            print(f"O motorista subiu na moto {moto.marca}.")
            moto.ligar()
        else:
            print("O motorista não possui o tipo de habilitação necessário para a moto.")

    def entrar_carro(self, carro):
        if "B" in self.habilitacao or "b" in self.habilitacao:
            print(f"O motorista entrou no carro {carro.marca}.")
            carro.ligar()
        else:
            print("O motorista não possui o tipo de habilitação necessário para o carro.")

carro = Carro("Chevette", 1990, 81, 5)
moto = Moto("Honda", 2022, 160, 5)

motorista1 = Motorista("A") 
motorista2 = Motorista("B")
motorista3 = Motorista("A e B")

motorista1.subir_moto(moto)
motorista2.entrar_carro(carro)
motorista3.entrar_carro(carro)
motorista3.subir_moto(moto)

carro.acelerar()
moto.acelerar()

carro.ligar()
moto.ligar()

carro.acelerar()  
moto.acelerar()   

carro.passar_marcha()
moto.passar_marcha()

carro.desligar()
moto.desligar()
