class Pessoa():
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def definir_nome(self, nome):
        self.nome = nome

    def definir_idade(self, idade):
        self.idade = idade

    def definir_altura(self, altura):
        self.altura = altura

    def obter_nome(self):
        return self.nome

    def obter_idade(self):
        return self.idade

    def obter_altura(self):
        return self.altura

    def cumprimentar(self):
        print(f"Olá, eu sou {self.nome}, tenho {self.idade} anos e {self.altura} de altura.")

if __name__=="__main__":
    pessoa = Pessoa("João", 30, 1.80)
    pessoa.cumprimentar()
    print(f"Nome: {pessoa.obter_nome()}")
    print(f"Idade: {pessoa.obter_idade()}")
    print(f"Altura: {pessoa.obter_altura()}")