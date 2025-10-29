from src.locadora import Filme, Usuario, FilmeIndisponivelError, LimiteEmprestimosExcedidoError

def main():
    print("=== SISTEMA LOCADORA AVANÇADO ===\n")
    
    # Criando catálogo de filmes
    filmes = [
        Filme("Interestelar", "Christopher Nolan", "978-85-123-4567-8"),
        Filme("O Poderoso Chefão", "Francis Ford Coppola", "978-85-234-5678-9"),
        Filme("O Senhor dos Anéis", "Peter Jackson", "978-85-345-6789-0"),
        Filme("Harry Potter", "Chris Columbus", "978-85-456-7890-1"),
        Filme("Orgulho e Preconceito", "Joe Wright", "978-85-567-8901-2"),
        Filme("O Pequeno Príncipe", "Mark Osborne", "978-85-678-9012-3")
    ]
    
    # Criando usuários
    usuario1 = Usuario("João Silva", 1)
    usuario2 = Usuario("Maria Santos", 2)
    
    # Demonstração interativa
    try:
        print("1. João pegando 3 filmes:")
        print(usuario1.pegar_emprestado(filmes[0]))
        print(usuario1.pegar_emprestado(filmes[1]))
        print(usuario1.pegar_emprestado(filmes[2]))
        
        print(f"\nStatus João: {usuario1}")
        
        print("\n2. Maria tentando pegar filme emprestado (deve funcionar):")
        print(usuario2.pegar_emprestado(filmes[3]))
        print(f"Status Maria: {usuario2}")
        
        print("\n3. João tentando pegar quarto filme (deve falhar):")
        print(usuario1.pegar_emprestado(filmes[4]))
        
    except (FilmeIndisponivelError, LimiteEmprestimosExcedidoError) as e:
        print(f"❌ Erro: {e}")
    
    # Devoluções
    print("\n4. Devoluções:")
    print(usuario1.devolver_filme(filmes[0]))
    print(usuario1.devolver_filme(filmes[1]))
    
    print(f"\nStatus final João: {usuario1}")
    print(f"Status final Maria: {usuario2}")
    
    # Mostrar status de todos os filmes
    print("\n5. STATUS DO ACERVO:")
    for filme in filmes:
        print(f"  - {filme}")

if __name__ == "__main__":
    main()
