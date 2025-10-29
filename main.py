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
        Filme("Clube da Luta", "Drama", "David Fincher", 2, 1999, 139, 4),
        Filme("O Poderoso Chefão", "Crime", "Francis Ford Coppola", 3, 1972, 175, 3),
        Filme("Matrix", "Sci-Fi", "Lana e Lilly Wachowski", 4, 1999, 136, 5),
        Filme("Star Wars: Episódio IV - Uma Nova Esperança", "Sci-Fi", "George Lucas", 5, 1977, 121, 4),
        Filme("De Volta para o Futuro", "Aventura", "Robert Zemeckis", 6, 1985, 116, 3),
        Filme("O Senhor dos Anéis: A Sociedade do Anel", "Fantasia", "Peter Jackson", 7, 2001, 178, 4),
        Filme("Forrest Gump", "Drama", "Robert Zemeckis", 8, 1994, 142, 3),
        Filme("Pulp Fiction", "Crime", "Quentin Tarantino", 9, 1994, 154, 4),
        Filme("O Silêncio dos Inocentes", "Thriller", "Jonathan Demme", 10, 1991, 118, 3),
        Filme("Gladiador", "Ação", "Ridley Scott", 11, 2000, 155, 4),
        Filme("Jurassic Park", "Aventura", "Steven Spielberg", 12, 1993, 127, 5),
        Filme("O Rei Leão", "Animação", "Roger Allers", 13, 1994, 88, 3),
        Filme("Toy Story", "Animação", "John Lasseter", 14, 1995, 81, 3),
        Filme("Titanic", "Romance", "James Cameron", 15, 1997, 195, 4),
        Filme("E.T. - O Extraterrestre", "Família", "Steven Spielberg", 16, 1982, 115, 3),
        Filme("Os Bons Companheiros", "Crime", "Martin Scorsese", 17, 1990, 146, 3),
        Filme("O Exorcista", "Terror", "William Friedkin", 18, 1973, 122, 2),
        Filme("A Origem", "Sci-Fi", "Christopher Nolan", 19, 2010, 148, 4),
        Filme("2001: Uma Odisseia no Espaço", "Sci-Fi", "Stanley Kubrick", 20, 1968, 149, 3)
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
        print(usuario1.pegar_emprestado(filmes[0]))  # Interestelar
        print(usuario1.pegar_emprestado(filmes[1]))  # Clube da Luta
        print(usuario1.pegar_emprestado(filmes[2]))  # O Poderoso Chefão
        print(f"\nStatus João: {usuario1}")

        # Maria pegando 1 filme
        print("\n2. Maria tentando pegar filme emprestado:")
        print(usuario2.pegar_emprestado(filmes[3]))  # Matrix
        print(f"Status Maria: {usuario2}")

        # João tentando pegar 4º filme (deve falhar)
        print("\n3. João tentando pegar quarto filme:")
        print(usuario1.pegar_emprestado(filmes[4]))  # Star Wars

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
