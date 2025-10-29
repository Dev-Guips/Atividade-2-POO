# test_locadora.py
import pytest
from datetime import datetime, timedelta
from src.locadora import Filme, Usuario, LimiteEmprestimosExcedidoError, FilmeEmprestarIndisponivelError

# ==============================
# TESTES FUNCIONAIS
# ==============================

def test_emprestar_e_devolver_filme():
    """
    Testa empréstimo e devolução de um filme dentro do prazo.
    """
    usuario = Usuario("João", 1)
    filme = Filme("Interestelar", "Sci-Fi", "Christopher Nolan", 1, 2014, 169, 1)

    # Emprestar filme
    resultado_emprestimo = usuario.pegar_emprestado(filme)
    assert resultado_emprestimo == f"Filme '{filme.nome}' emprestado com sucesso"
    assert filme.disponivel == False
    assert filme in usuario.filmes_emprestados

    # Devolver filme dentro do prazo
    resultado_devolucao = usuario.devolver_filme(filme)
    assert resultado_devolucao == "Filme devolvido dentro do prazo"
    assert filme.disponivel == True
    assert filme not in usuario.filmes_emprestados

def test_limite_emprestimos():
    """
    Testa que o usuário não pode pegar mais de 3 filmes.
    """
    usuario = Usuario("Maria", 2)
    filmes = [
        Filme("Filme 1", "Ação", "Diretor 1", 2, 2020, 120, 1),
        Filme("Filme 2", "Ação", "Diretor 2", 3, 2020, 120, 1),
        Filme("Filme 3", "Ação", "Diretor 3", 4, 2020, 120, 1),
    ]

    # Empresta 3 filmes normalmente
    for f in filmes:
        usuario.pegar_emprestado(f)

    # Tentar pegar o 4º filme deve gerar exceção
    with pytest.raises(LimiteEmprestimosExcedidoError):
        filme_extra = Filme("Filme 4", "Ação", "Diretor 4", 5, 2020, 120, 1)
        usuario.pegar_emprestado(filme_extra)

def test_filme_indisponivel():
    """
    Testa que não é possível emprestar um filme que já está emprestado.
    """
    usuario1 = Usuario("Alice", 3)
    usuario2 = Usuario("Bob", 4)
    filme = Filme("Matrix", "Sci-Fi", "Wachowski", 6, 1999, 136, 1)

    usuario1.pegar_emprestado(filme)

    # Segundo usuário tenta pegar e deve gerar exceção
    with pytest.raises(FilmeEmprestarIndisponivelError):
        usuario2.pegar_emprestado(filme)

def test_devolver_filme_nao_emprestado():
    """
    Testa que não é possível devolver um filme que não foi emprestado.
    """
    usuario = Usuario("Carlos", 5)
    filme = Filme("O Senhor dos Anéis", "Fantasia", "Peter Jackson", 7, 2001, 178, 1)

    # Devolver filme não emprestado gera exceção
    with pytest.raises(Exception):
        usuario.devolver_filme(filme)

# ==============================
# TESTE PROPOSITAL QUE FALHA
# ==============================
def test_erro_proposital():
    """
    Teste proposital que tenta pegar mais de 3 filmes.
    Deve gerar erro de limite de empréstimos.
    """
    usuario = Usuario("Teste", 99)
    filme1 = Filme("Filme 1", "Ação", "Diretor 1", 8, 2020, 120, 1)
    filme2 = Filme("Filme 2", "Ação", "Diretor 2", 9, 2020, 120, 1)
    filme3 = Filme("Filme 3", "Ação", "Diretor 3", 10, 2020, 120, 1)
    filme4 = Filme("Filme 4", "Ação", "Diretor 4", 11, 2020, 120, 1)

    # Emprestando 3 filmes
    usuario.pegar_emprestado(filme1)
    usuario.pegar_emprestado(filme2)
    usuario.pegar_emprestado(filme3)

    # Tentativa de pegar quarto filme (falha proposital)
    usuario.pegar_emprestado(filme4)

# ==============================
# TESTE DE MULTA POR ATRASO
# ==============================
def test_filme_em_atraso():
    """
    Testa a devolução de um filme após o prazo, gerando multa.
    """
    usuario = Usuario("Pedro", 6)
    filme = Filme("Interestelar", "Sci-Fi", "Christopher Nolan", 12, 2014, 169, 1)

    # Empresta o filme
    usuario.pegar_emprestado(filme)

    # Simula atraso: ajusta a data de empréstimo para 20 dias atrás
    # Prazo de empréstimo = 15 dias
    # Dias de atraso = 20 - 15 = 5 dias
    # Multa = R$ 1,00 por dia -> multa total = R$ 5,00
    filme.data_emprestimo -= timedelta(days=20)

    # Devolver filme e calcular multa
    resultado = usuario.devolver_filme(filme)
    assert "multa" in resultado  # Deve ter multa
    print(resultado)  # Deve mostrar: "Filme devolvido com multa de R$ 5.00"
