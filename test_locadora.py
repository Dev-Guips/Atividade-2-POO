import pytest
from datetime import datetime, timedelta
from src.locadora import Filme, Usuario, FilmeEmprestarIndisponivelError, LimiteEmprestimosExcedidoError

# --------------------------
# FIXTURES
# --------------------------
@pytest.fixture
def filmes():
    return [
        Filme("Interestelar", "Sci-Fi", "Christopher Nolan", 1, 2014, 169, 5),
        Filme("Matrix", "Sci-Fi", "Lana e Lilly Wachowski", 2, 1999, 136, 5),
        Filme("O Poderoso Chefão", "Crime", "Francis Ford Coppola", 3, 1972, 175, 3),
    ]

@pytest.fixture
def usuario():
    return Usuario("João Silva", 1)

# --------------------------
# TESTES
# --------------------------

def test_emprestar_filme_disponivel(usuario, filmes):
    # João pega um filme disponível
    resultado = usuario.pegar_emprestado(filmes[0])
    assert filmes[0] in usuario.filmes_emprestados
    assert not filmes[0].disponivel
    assert "emprestado com sucesso" in resultado

def test_emprestar_filme_indisponivel(usuario, filmes):
    # Empresta o filme uma vez
    usuario.pegar_emprestado(filmes[0])
    # Tentar emprestar novamente deve gerar exceção
    with pytest.raises(FilmeEmprestarIndisponivelError):
        filmes[0].emprestar()

def test_limite_emprestimos(usuario, filmes):
    # Empresta 3 filmes
    usuario.pegar_emprestado(filmes[0])
    usuario.pegar_emprestado(filmes[1])
    usuario.pegar_emprestado(filmes[2])
    # Tentativa de pegar 4º filme gera exceção
    novo_filme = Filme("Star Wars", "Sci-Fi", "George Lucas", 4, 1977, 121, 2)
    with pytest.raises(LimiteEmprestimosExcedidoError):
        usuario.pegar_emprestado(novo_filme)

def test_devolver_filme_dentro_prazo(usuario, filmes):
    usuario.pegar_emprestado(filmes[0])
    multa = usuario.devolver_filme(filmes[0])
    assert multa == "Filme devolvido dentro do prazo"
    assert filmes[0].disponivel
    assert filmes[0] not in usuario.filmes_emprestados

def test_calcular_multa(usuario):
    # Criar filme e simular atraso
    filme = Filme("Titanic", "Romance", "James Cameron", 5, 1997, 195, 2)
    usuario.pegar_emprestado(filme)
    # Simula que foi emprestado há 20 dias
    filme.data_emprestimo -= timedelta(days=20)
    multa = usuario.devolver_filme(filme)
    assert "multa" in multa  # Deve gerar multa
