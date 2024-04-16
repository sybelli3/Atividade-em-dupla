class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.estado ="desligado"
        
    def ligar(self):
        self.estado= "ligado"
        print("o carro esta ligado")

    def desligar(self):
        self.estado = "desligado"
        print("o carro esta desligado")
        
    def acelerando(self, velocidade):
        if self.estado == "ligado":
            print(f"o carro esta acerelando para {velocidade} km/h")
        else:
            print("o carro esta dessligado. nao e possivel acelerar")
        

if __name__=="__main__":
    carro = Carro("Fiat", "Uno", "2010")
    carro.ligar()
    carro.acelerando(100)
    carro.desligar()