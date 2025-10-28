from src.biblioteca import Livro, Usuario, LivroIndisponivelError, LimiteEmprestimosExcedidoError

def main():
    print("=== SISTEMA BIBLIOTECA AVANÇADO ===\n")
    
    # Criando catálogo de livros
    livros = [
        Livro("Dom Casmurro", "Machado de Assis", "978-85-123-4567-8"),
        Livro("1984", "George Orwell", "978-85-234-5678-9"),
        Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "978-85-345-6789-0"),
        Livro("Harry Potter", "J.K. Rowling", "978-85-456-7890-1"),
        Livro("Orgulho e Preconceito", "Jane Austen", "978-85-567-8901-2"),
        Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "978-85-678-9012-3")
    ]
    
    # Criando usuários
    usuario1 = Usuario("João Silva", 1)
    usuario2 = Usuario("Maria Santos", 2)
    
    # Demonstração interativa
    try:
        print("1. João pegando 3 livros:")
        print(usuario1.pegar_emprestado(livros[0]))
        print(usuario1.pegar_emprestado(livros[1]))
        print(usuario1.pegar_emprestado(livros[2]))
        
        print(f"\nStatus João: {usuario1}")
        
        print("\n2. Maria tentando pegar livro emprestado (deve funcionar):")
        print(usuario2.pegar_emprestado(livros[3]))
        print(f"Status Maria: {usuario2}")
        
        print("\n3. João tentando pegar quarto livro (deve falhar):")
        print(usuario1.pegar_emprestado(livros[4]))
        
    except (LivroIndisponivelError, LimiteEmprestimosExcedidoError) as e:
        print(f"❌ Erro: {e}")
    
    # Devoluções
    print("\n4. Devoluções:")
    print(usuario1.devolver_livro(livros[0]))
    print(usuario1.devolver_livro(livros[1]))
    
    print(f"\nStatus final João: {usuario1}")
    print(f"Status final Maria: {usuario2}")
    
    # Mostrar status de todos os livros
    print("\n5. STATUS DO ACERVO:")
    for livro in livros:
        print(f"  - {livro}")

if __name__ == "__main__":
    main()