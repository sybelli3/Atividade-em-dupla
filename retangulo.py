class Retangulo():
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        area = self.altura * self.largura
        print(f"A área do retângulo é de {area} unidades.")

    def calcular_perimetro(self):
        perimetro = 2 * (self.altura + self.largura)
        print(f"O perímetro do retângulo é de {perimetro} unidades.")

if __name__=="__main__":
    retangulo = Retangulo(5, 10)
    retangulo.calcular_area()
    retangulo.calcular_perimetro()