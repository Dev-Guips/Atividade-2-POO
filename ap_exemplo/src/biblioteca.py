# --------------------------
# IMPORT
# --------------------------
from datetime import datetime, timedelta


# -----------------------------------------------
# EXCEÇÕES PERSONALIZADAS (Tratamento de Erros)
# -----------------------------------------------

# SABER ONDE USAR CADA EXCEÇÃO QUE VAMOS CRIAR:

# Exeção Base -> Tentar remover um filme que não existe / Tentar acessar um ID inválido
class LocadoraError(Exception): 
    pass

#  Usuário exceder limite de empréstimos
class LimiteEmprestimosExcedidoError(LocadoraError):
    #Usar na class usuario, no método emprestar
    pass

# Tentar devolver filme não emprestado (Filme não pode ser devolvido se -> / Se tentar devolver algo que não pertence ao user)
class FilmeDevolverIndisponivelError(LocadoraError):
    # Não está emprestado
    # OU não foi emprestado por ele
    pass


# Tentar emprestar filme indisponível (Filme não pode ser emprestado)
class FilmeEmprestarIndisponivelError(LocadoraError):
  # Usado no metro emprestar() do filme quando:
  # disponivel == False
  #qtd_disponivel == 0
  pass


# --------------------------
# CLASSE LOCADORA
# --------------------------
class Locadora:
  def __init__(self):
    self.catalogo = {}

  # --------------------------
  # MÉTODOS DA CLASSE LOCADORA
  # --------------------------

  def adicionar_filme(self, filme):
    id_filme = filme.id_filme
    if id_filme in self.catalogo:
      raise LocadoraError("Filme com este ID já existe no catálogo")
    self.catalogo[id_filme] = filme
    print(f"Filme '{filme.nome}' adicionado com sucesso!✅")

  def remover_filme(self, id_filme):
    if id_filme not in self.catalogo:
      raise LocadoraError(f"Filme '{id_filme}' não encontrado ❌")
    del self.catalogo[id_filme]
    print(f"Filme com ID {id_filme} removido com sucesso!✅")

  def buscar_filme(self, id_filme):
    if id_filme not in self.catalogo:
      raise LocadoraError(f"Filme {id_filme} não encontrado em catalogo")
    return self.catalogo[id_filme]


# --------------------------
# CLASSE FILME
# --------------------------

class Filme:
  #Atributos da class Filmes
  def __init__(self, nome:str, genero:str, autor:str, id_filme:int, ano_lancamento:int, duracao:int, qtd_disponivel:int):
    self.nome = nome
    self.genero = genero
    self.autor = autor
    self.id_filme = id_filme
    self.ano_lancamento = ano_lancamento
    self.duracao = duracao
    self.qtd_disponivel = qtd_disponivel
    self.disponivel = True
    self.data_emprestimo = None


  # --------------------------
  # MÉTODOS DA CLASSE FILME
  # --------------------------

  def emprestar(self):
    if not self.disponivel:
      raise FilmeEmprestarIndisponivelError(f"Filme '{self.nome}' não está disponível para emprestimo no momento") # Funcionalidade Implementar se der tempo {colocar quanto tempo vai estar disponivel para a pessoa pegar emprestado}
    self.disponivel = False
    self.data_emprestimo = datetime.now()


  def devolver(self):
    if self.disponivel:
      raise FilmeDevolverIndisponivelError(f"Filme'{self.nome}' não está disponível")
    self.disponivel = True
    return self.calcular_multa()


  def calcular_multa(self):
    if self.data_emprestimo:
      dias_emprestimo = (datetime.now() - self.data_emprestimo).days
      if dias_emprestimo > 15: # Prazo de 15 dias
        return (dias_emprestimo - 15) *1.0 # MULTA -> R$ 1,00 por dia
    return 0.0

  def __str__(self):
    status = "Disponível" if self.disponivel else "Emprestado"
    return f"'{self.nome}' - {self.autor} [{status}]"


# CLASSE USUARIO (Capítulo 7)
# class Usuario:
#     def __init__(self, nome: str, id_usuario: int):
#         self.nome = nome
#         self.id = id_usuario
#         self.livros_emprestados = []

#     def pegar_emprestado(self, livro: Livro):
#         if len(self.livros_emprestados) >= 3:
#             raise LimiteEmprestimosExcedidoError(
#                 f"Usuário {self.nome} excedeu o limite de 3 empréstimos"
#             )

#         livro.emprestar()
#         self.livros_emprestados.append(livro)
#         return f"Livro '{livro.titulo}' emprestado com sucesso"

#     def devolver_livro(self, livro: Livro):
#         if livro not in self.livros_emprestados:
#             raise BibliotecaError(f"Livro '{livro.titulo}' não foi emprestado por este usuário")

#         multa = livro.devolver()
#         self.livros_emprestados.remove(livro)

#         if multa > 0:
#             return f"Livro devolvido com multa de R$ {multa:.2f}"
#         return "Livro devolvido dentro do prazo"

#     def __str__(self):
#         livros_titulos = [livro.titulo for livro in self.livros_emprestados]
#         return f"Usuário: {self.nome} (ID: {self.id}) - Livros: {len(self.livros_emprestados)} - {livros_titulos}"


# EXEMPLO DE USO
if __name__ == "__main__":
    
#Criação de objetos

    locadora = Locadora()
    filme1 = Filme("Matrix", "Sci-Fi", "Wachowski", 1, 1999, 136, 5)
    filme2 = Filme("Alien", "Sci-Fi", "Messi", 2, 2009, 206, 3)
    filme3 = Filme("Um dia no parque", "Brincadeiras com a minha vizinha", "Turing", 3, 2019, 236, 8)
    filme4 = Filme("O nerd dahora", "Sci-Fi", "Gab", 4, 2014, 136, 7)
    # Adicionar o filme funciona

    # locadora.adicionar_filme(filme1)
    # locadora.adicionar_filme(filme2)
    # locadora.adicionar_filme(filme3)
    # locadora.adicionar_filme(filme4)

    #ADICIONAR FILMES
    for film in [filme1, filme2, filme3, filme4]:
        try:
            locadora.adicionar_filme(film)
        except LocadoraError as e:
            print(f"Erro ao adicionar: {e}")

    #TENTAR ADICIONAR DE NOVO
    try:
        locadora.adicionar_filme(filme1)
    except LocadoraError as e:
        print(f"Erro ao adicionar novamente: {e}")


# REMOVER FILME EXISTENTE(FILME1) E FILME INEXISTENTE (ID_FILME = 0):
try:
  locadora.remover_filme(filme1.id_filme)
  locadora.remover_filme(0)
except LocadoraError as e:
  print(f"Erro de remover ID 0: {e}")

# BUSCAR FILME
filmeh = locadora.buscar_filme(filme2.id_filme)
print(f"O filme {filmeh}")

filmer = locadora.buscar_filme(filme3.id_filme)
print(filmer)# Nesta parte vale mudar o return do metodo buscar_filme


usuario = Usuario("João Silva", 1)

try:
    print("=== SISTEMA LOCADORA ===\n")
    print(usuario.pegar_emprestado(filme1))
    print(usuario.pegar_emprestado(filme2))
    print(usuario.pegar_emprestado(filme3))

    print(f"\nStatus do usuário: {usuario}")

    # Tentativa de pegar quarto livro (deve falhar)
    print("\nTentando pegar quarto filme...")
    print(usuario.pegar_emprestado(filme4))

except (FilmeIndisponivelError, LimiteEmprestimosExcedidoError) as e:
    print(f"Erro: {e}")

print("\n=== DEVOLUÇÃO DE FILMES ===")
print(usuario.devolver_filme(filme1))
print(f"Status após devolução: {filme1}")
print(f"Status do usuário: {usuario}")
