from datetime import datetime, timedelta

# EXCEÇÃO PERSONALIZADA (Capítulo 9)
class BibliotecaError(Exception):
    pass

class LimiteEmprestimosExcedidoError(BibliotecaError):
    pass

class LivroIndisponivelError(BibliotecaError):
    pass

# CLASSE LIVRO (Capítulo 7)
class Livro:
    def __init__(self, titulo: str, autor: str, isbn: str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True
        self.data_emprestimo = None
    
    def emprestar(self):
        if not self.disponivel:
            raise LivroIndisponivelError(f"Livro '{self.titulo}' não está disponível")
        self.disponivel = False
        self.data_emprestimo = datetime.now()
    
    def devolver(self):
        if self.disponivel:
            raise BibliotecaError(f"Livro '{self.titulo}' já está disponível")
        self.disponivel = True
        return self.calcular_multa()
    
    def calcular_multa(self):
        if self.data_emprestimo:
            dias_emprestimo = (datetime.now() - self.data_emprestimo).days
            if dias_emprestimo > 14:  # Prazo de 14 dias
                return (dias_emprestimo - 14) * 1.0  # R$ 1,00 por dia
        return 0.0
    
    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' - {self.autor} [{status}]"

# CLASSE USUARIO (Capítulo 7)
class Usuario:
    def __init__(self, nome: str, id_usuario: int):
        self.nome = nome
        self.id = id_usuario
        self.livros_emprestados = []
    
    def pegar_emprestado(self, livro: Livro):
        if len(self.livros_emprestados) >= 3:
            raise LimiteEmprestimosExcedidoError(
                f"Usuário {self.nome} excedeu o limite de 3 empréstimos"
            )
        
        livro.emprestar()
        self.livros_emprestados.append(livro)
        return f"Livro '{livro.titulo}' emprestado com sucesso"
    
    def devolver_livro(self, livro: Livro):
        if livro not in self.livros_emprestados:
            raise BibliotecaError(f"Livro '{livro.titulo}' não foi emprestado por este usuário")
        
        multa = livro.devolver()
        self.livros_emprestados.remove(livro)
        
        if multa > 0:
            return f"Livro devolvido com multa de R$ {multa:.2f}"
        return "Livro devolvido dentro do prazo"
    
    def __str__(self):
        livros_titulos = [livro.titulo for livro in self.livros_emprestados]
        return f"Usuário: {self.nome} (ID: {self.id}) - Livros: {len(self.livros_emprestados)} - {livros_titulos}"

# EXEMPLO DE USO
if __name__ == "__main__":
    # Criando livros e usuários
    livro1 = Livro("Dom Casmurro", "Machado de Assis", "978-85-123-4567-8")
    livro2 = Livro("1984", "George Orwell", "978-85-234-5678-9")
    livro3 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "978-85-345-6789-0")
    livro4 = Livro("Harry Potter", "J.K. Rowling", "978-85-456-7890-1")
    
    usuario = Usuario("João Silva", 1)
    
    # Testando funcionalidades
    try:
        print("=== SISTEMA BIBLIOTECA ===\n")
        print(usuario.pegar_emprestado(livro1))
        print(usuario.pegar_emprestado(livro2))
        print(usuario.pegar_emprestado(livro3))
        
        print(f"\nStatus do usuário: {usuario}")
        
        # Tentativa de pegar quarto livro (deve falhar)
        print("\nTentando pegar quarto livro...")
        print(usuario.pegar_emprestado(livro4))
        
    except (LivroIndisponivelError, LimiteEmprestimosExcedidoError) as e:
        print(f"Erro: {e}")
    
    # Devolvendo livros
    print("\n=== DEVOLUÇÃO DE LIVROS ===")
    print(usuario.devolver_livro(livro1))
    print(f"Status após devolução: {livro1}")
    print(f"Status do usuário: {usuario}")