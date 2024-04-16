import math

class Triangulo():
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def calcular(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        print(f"A área do triângulo é de {area} unidades.")

    def calcular(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        print(f"O perímetro do triângulo é de {perimetro} unidades.")

if __name__=="__main__":
    triangulo = Triangulo(3, 4, 5)
    triangulo.calcular()
    triangulo.calcular()