# --------------------------
# IMPORTS
# --------------------------
from src.locadora import Filme, Usuario, FilmeEmprestarIndisponivelError, LimiteEmprestimosExcedidoError

# --------------------------
# FUNÇÃO PRINCIPAL
# --------------------------
def main():
    print("=== SISTEMA LOCADORA AVANÇADO ===\n")

    # --------------------------
    # Criando catálogo de filmes
    # --------------------------
    filmes = [
        Filme("Interestelar", "Sci-Fi", "Christopher Nolan", 1, 2014, 169, 5),
        Filme("O Poderoso Chefão", "Crime", "Francis Ford Coppola", 2, 1972, 175, 3),
        Filme("O Senhor dos Anéis", "Fantasia", "Peter Jackson", 3, 2001, 178, 4),
        Filme("Harry Potter", "Fantasia", "Chris Columbus", 4, 2001, 152, 6),
        Filme("Orgulho e Preconceito", "Romance", "Joe Wright", 5, 2005, 129, 2),
        Filme("O Pequeno Príncipe", "Animação", "Mark Osborne", 6, 2015, 108, 3)
    ]

    # --------------------------
    # Criando usuários
    # --------------------------
    usuario1 = Usuario("João Silva", 1)
    usuario2 = Usuario("Maria Santos", 2)

    # --------------------------
    # Demonstração interativa
    # --------------------------
    try:
        # João pegando 3 filmes
        print("1. João pegando 3 filmes:")
        print(usuario1.pegar_emprestado(filmes[0]))
        print(usuario1.pegar_emprestado(filmes[1]))
        print(usuario1.pegar_emprestado(filmes[2]))
        print(f"\nStatus João: {usuario1}")

        # Maria pegando 1 filme
        print("\n2. Maria tentando pegar filme emprestado:")
        print(usuario2.pegar_emprestado(filmes[3]))
        print(f"Status Maria: {usuario2}")

        # João tentando pegar 4º filme (deve falhar)
        print("\n3. João tentando pegar quarto filme:")
        print(usuario1.pegar_emprestado(filmes[4]))

    except (FilmeEmprestarIndisponivelError, LimiteEmprestimosExcedidoError) as e:
        print(f"❌ Erro: {e}")

    # --------------------------
    # Devoluções
    # --------------------------
    print("\n4. Devoluções:")
    print(usuario1.devolver_filme(filmes[0]))
    print(usuario1.devolver_filme(filmes[1]))
    print(f"\nStatus final João: {usuario1}")
    print(f"Status final Maria: {usuario2}")

    # --------------------------
    # Mostrar status de todos os filmes
    # --------------------------
    print("\n5. STATUS DO ACERVO:")
    for filme in filmes:
        print(f"  - {filme}")

# --------------------------
# EXECUTANDO O PROGRAMA
# --------------------------
if __name__ == "__main__":
    main()
