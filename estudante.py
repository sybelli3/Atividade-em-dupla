class Estudante():
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        media = sum(self.notas) / len(self.notas)
        print(f"A média do estudante {self.nome} é {media}.")

    def mostrar_situacao(self):
        media = sum(self.notas) / len(self.notas)
        if media >= 7:
            situacao = "aprovado"
        else:
            situacao = "reprovado"
        print(f"O estudante {self.nome} está {situacao}.")

if __name__=="__main__":
    estudante = Estudante("João", 18, [8, 7, 9, 10])
    estudante.calcular_media()
    estudante.mostrar_situacao()