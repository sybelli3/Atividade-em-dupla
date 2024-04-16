class Pedido():
    def __init__(self):
        self.itens = []
        self.total = 0
        self.status = "aberto"

    def adicionar_item(self, item, preco):
        self.itens.append(item)
        self.total += preco
        print(f"O item {item} foi adicionado ao pedido. O total é de R${self.total}.")

    def calcular_total(self):
        print(f"O total do pedido é de R${self.total}.")

    def alterar_status(self, status):
        self.status = status
        print(f"O status do pedido foi alterado para {self.status}.")

if __name__=="__main__":
    pedido = Pedido()
    pedido.adicionar_item("Coca-Cola", 5)
    pedido.adicionar_item("Pizza", 30)
    pedido.calcular_total()
    pedido.alterar_status("fechado")