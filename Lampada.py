class Lampada:
    def __init__(self, marca, tipo, brilho):
        self.marca = marca
        self.tipo = tipo
        self.is_running = False
        self.set_brilho(brilho)

    # Ligando a lampada
    def ligar(self):
        if not self.is_running:
            self.is_running = True
            print(f"A lâmpada está ligada, brilho: {self.brilho} lúmens")
        else:
            print("A lâmpada já está ligada.")

    # Desligando a lampada
    def desligar(self):
        if self.is_running:
            self.is_running = False
            print("A lâmpada está desligada.")
        else:
            print("A lâmpada já está desligada.")

    # Ajustando o brilho
    def ajustar_brilho(self, novo_brilho):
        if self.is_running:
            self.set_brilho(novo_brilho)
            print(f"O brilho da lâmpada foi ajustado para {self.brilho} lúmens")
        else:
            print("A lâmpada está desligada, precisa ligar primeiro.")

    def set_brilho(self, brilho):
        if brilho < 0:
            self.brilho = 0
        elif brilho > 1000:
            self.brilho = 1000
        else:
            self.brilho = brilho

    def __str__(self):
        return f"Lampada [marca={self.marca}, tipo={self.tipo}, is_running={self.is_running}, brilho={self.brilho}]"


if __name__ == "__main__":
    lampada = Lampada("Philips", "LED", 800)
    print(lampada)

    lampada.ajustar_brilho(600)
    lampada.ligar()
    lampada.ajustar_brilho(600)
    lampada.ajustar_brilho(1000)
    lampada.desligar()
    lampada.ajustar_brilho(500)
