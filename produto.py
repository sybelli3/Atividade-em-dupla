class Produto():
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        
    def atualizar(self, quantitade):
        self.estoque -= quantitade
        print(f"o preco atual do produto{self.nome} e de {self.estoque} unidade")
        
    def calcular (self, quantidade):
        preco1= self.preco * quantidade
        print (f"o preco total do produto {self.nome} e de R$ {preco1}")
if __name__=="__main__":
    produto = Produto("Livro", 50, 100)
    produto.atualizar(10)
    produto.calcular(5)
    