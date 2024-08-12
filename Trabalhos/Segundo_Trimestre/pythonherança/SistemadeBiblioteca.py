class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        self.disponivel = True

    def __str__(self):
        disponibilidade = 'Disponível' if self.disponivel else 'Indisponível'
        return f'Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, {disponibilidade}'


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def mostrar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
        for livro in self.livros:
            print(livro)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.emprestar():
                    print(f'Livro "{titulo}" emprestado com sucesso.')
                else:
                    print(f'Livro "{titulo}" não está disponível.')
                return
        print(f'Livro "{titulo}" não encontrado.')

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.devolver()
                print(f'Livro "{titulo}" devolvido com sucesso.')
                return
        print(f'Livro "{titulo}" não encontrado.')




biblioteca = Biblioteca()

livro1 = Livro("O Hobbit", "J.R.R. Tolkien", 1937)
livro2 = Livro("1984", "George Orwell", 1949)

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

print("Livros na biblioteca:")
biblioteca.mostrar_livros()

print("\nTentando emprestar 'O Hobbit':")
biblioteca.emprestar_livro("O Hobbit")

print("\nLivros na biblioteca após o empréstimo:")
biblioteca.mostrar_livros()

print("\nTentando devolver 'O Hobbit':")
biblioteca.devolver_livro("O Hobbit")

print("\nLivros na biblioteca após a devolução:")
biblioteca.mostrar_livros()
