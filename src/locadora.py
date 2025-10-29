# --------------------------
# IMPORTS
# --------------------------
from datetime import datetime, timedelta

# -----------------------------------------------
# EXCEÇÕES PERSONALIZADAS (Tratamento de Erros)
# -----------------------------------------------

class LocadoraError(Exception):
    """Exceção base para erros da locadora."""
    pass

class LimiteEmprestimosExcedidoError(LocadoraError):
    """Erro quando o usuário excede o limite de filmes emprestados."""
    pass

class FilmeDevolverIndisponivelError(LocadoraError):
    """Erro quando se tenta devolver um filme que não foi emprestado."""
    pass

class FilmeEmprestarIndisponivelError(LocadoraError):
    """Erro quando se tenta emprestar um filme indisponível."""
    pass

# --------------------------
# CLASSE LOCADORA
# --------------------------
class Locadora:
    """Gerencia o catálogo de filmes da locadora."""

    def __init__(self):
        self.catalogo = {}  # Dicionário de filmes {id_filme: filme}

    def adicionar_filme(self, filme):
        """Adiciona um filme ao catálogo."""
        id_filme = filme.id_filme
        if id_filme in self.catalogo:
            raise LocadoraError("Filme com este ID já existe no catálogo")
        self.catalogo[id_filme] = filme
        print(f"Filme '{filme.nome}' adicionado com sucesso! ✅")

    def remover_filme(self, id_filme):
        """Remove um filme do catálogo pelo ID."""
        if id_filme not in self.catalogo:
            raise LocadoraError(f"Filme '{id_filme}' não encontrado ❌")
        del self.catalogo[id_filme]
        print(f"Filme com ID {id_filme} removido com sucesso! ✅")

    def buscar_filme(self, id_filme):
        """Busca e retorna um filme pelo ID."""
        if id_filme not in self.catalogo:
            raise LocadoraError(f"Filme {id_filme} não encontrado em catálogo")
        return self.catalogo[id_filme]

# --------------------------
# CLASSE FILME
# --------------------------
class Filme:
    """Representa um filme disponível na locadora."""

    def __init__(self, nome: str, genero: str, autor: str, id_filme: int, ano_lancamento: int, duracao: int, qtd_disponivel: int):
        self.nome = nome
        self.genero = genero
        self.autor = autor
        self.id_filme = id_filme
        self.ano_lancamento = ano_lancamento
        self.duracao = duracao
        self.qtd_disponivel = qtd_disponivel
        self.disponivel = True
        self.data_emprestimo = None

    def emprestar(self):
        """Marca o filme como emprestado e registra a data do empréstimo."""
        if not self.disponivel:
            raise FilmeEmprestarIndisponivelError(f"Filme '{self.nome}' não está disponível para empréstimo")
        self.disponivel = False
        self.data_emprestimo = datetime.now()

    def devolver(self):
        """Marca o filme como disponível e calcula multa, se houver."""
        if self.disponivel:
            raise FilmeDevolverIndisponivelError(f"Filme '{self.nome}' não está disponível para devolução")
        self.disponivel = True
        return self.calcular_multa()

    def calcular_multa(self):
        """Calcula multa caso o filme seja devolvido após 15 dias."""
        if self.data_emprestimo:
            dias_emprestimo = (datetime.now() - self.data_emprestimo).days
            if dias_emprestimo > 15:
                return (dias_emprestimo - 15) * 1.0  # R$1,00 por dia de atraso
        return 0.0

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.nome}' - {self.autor} [{status}]"

# --------------------------
# CLASSE USUÁRIO
# --------------------------
class Usuario:
    """Representa um cliente da locadora."""

    def __init__(self, nome: str, id_usuario: int):
        self.nome = nome
        self.id = id_usuario
        self.filmes_emprestados = []  # Lista de filmes que o usuário pegou

    def pegar_emprestado(self, filme: Filme):
        """Empresta um filme, se ainda não ultrapassou o limite de 3 filmes."""
        if len(self.filmes_emprestados) >= 3:
            raise LimiteEmprestimosExcedidoError(
                f"Usuário {self.nome} excedeu o limite de 3 empréstimos"
            )
        filme.emprestar()
        self.filmes_emprestados.append(filme)
        return f"Filme '{filme.nome}' emprestado com sucesso"

    def devolver_filme(self, filme: Filme):
        """Devolve um filme e calcula multa, se houver."""
        if filme not in self.filmes_emprestados:
            raise LocadoraError(f"Filme '{filme.nome}' não foi emprestado por este usuário")
        multa = filme.devolver()
        self.filmes_emprestados.remove(filme)
        if multa > 0:
            return f"Filme devolvido com multa de R$ {multa:.2f}"
        return "Filme devolvido dentro do prazo"

    def __str__(self):
        filmes_titulos = [filme.nome for filme in self.filmes_emprestados]
        return f"Usuário: {self.nome} (ID: {self.id}) - Filmes: {len(self.filmes_emprestados)} - {filmes_titulos}"
