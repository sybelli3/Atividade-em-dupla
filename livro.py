class Livro():
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.palavras_pagina = 250
    def mostrar_informacoes(self):
        print(f"O título do livro é {self.titulo}, escrito por {self.autor} e tem {self.num_paginas} páginas.")
    
    def calcular_palavras__paginas(self):
        total_palavras = self.palavras_pagina * self.num_paginas
        print(f"O livro {self.titulo} tem aproximadamente {total_palavras} palavras.")
  
if __name__=="__main__":
    livro = Livro("A Guerra dos Tronos", "George R.R. Martin", 700)
    livro.mostrar_informacoes()
    livro.calcular_palavras__paginas()      