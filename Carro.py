class Carro:
    def __init__(self, marca, ano, num_marcha):
        self.marca = marca
        self.ano = ano
        self.ligado = False
        self.num_marcha = num_marcha
        self.velocidade = 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.marca} ligado.")
        else:
            print(f"{self.marca} já está ligado.")

    def desligar(self):
        if self.ligado:
            if self.velocidade > 0:
                print(f"{self.marca} está em movimento. Reduzindo a velocidade até parar...")
                while self.velocidade > 0: # só pro carro não desligar a 80 por hora...
                    self.velocidade -= 5
                    print(f"{self.marca} reduzindo a velocidade. Velocidade atual: {self.velocidade} km/h.")
                print(f"{self.marca} parou. Desligando...")
            else:
                print(f"{self.marca} está parado. Desligando.")
            self.ligado = False
        else:
            print(f"{self.marca} não está ligado, ligue-o antes.")

    def passar_marcha(self):
        if self.ligado:
            if self.velocidade == 0:
                print(f"{self.marca} passou para a marcha {self.num_marcha}.")
            elif self.velocidade > 0 and self.num_marcha < 5:
                self.num_marcha += 1
                print(f"{self.marca} passou para a marcha {self.num_marcha}.")
            else:
                print(f"{self.marca} já está na marcha máxima.")
        else:
            print(f"{self.marca} está desligado, impossível passar de marcha.")

    def acelerar(self):
        if self.ligado:
            if self.num_marcha == 1:
                aceleracao = 20
            elif self.num_marcha == 2:
                aceleracao = 30
            elif self.num_marcha == 3:
                aceleracao = 40
            elif self.num_marcha == 4:
                aceleracao = 60
            else:
                aceleracao = 80
            self.velocidade += aceleracao
            print(f"{self.marca} acelerando na marcha {self.num_marcha}. Velocidade: {self.velocidade} km/h.")
        else:
            print(f"{self.marca} não está ligado, precisa estar ligado para acelerar.")

    def marcha_re(self):
        if self.ligado:
            if self.velocidade == 0:
                print(f"{self.marca} está na marcha ré.")
            elif self.velocidade == 1:
                print(f"{self.marca} está na marcha ré a {self.velocidade} km/h.")
            else:
                print("A marcha ré só pode ser ativada a 1km/h ou menos!")
        else:
            print(f"{self.marca} está desligado, impossível colocar na marcha ré.")



carro = Carro("Chevette", 1993, 1)
carro.ligar()
carro.acelerar()
carro.passar_marcha()
carro.acelerar()
carro.marcha_re()
carro.desligar()
