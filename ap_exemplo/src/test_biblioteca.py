from datetime import datetime, timedelta

# EXCEÇÃO PERSONALIZADA (Capítulo 9)
class LocadoraError(Exception):
    pass

class LimiteEmprestimosExcedidoError(LocadoraError):
    pass

class FilmeIndisponivelError(LocadoraError):
    pass

# CLASSE FILME (Capítulo 7)
class Filme:
    def __init__(self, titulo: str, diretor: str, codigo: str):
        self.titulo = titulo
        self.diretor = diretor
        self.codigo = codigo
        self.disponivel = True
        self.data_emprestimo = None
    
    def emprestar(self):
        if not self.disponivel:
            raise FilmeIndisponivelError(f"Filme '{self.titulo}' não está disponível")
        self.disponivel = False
        self.data_emprestimo = datetime.now()
    
    def devolver(self):
        if self.disponivel:
            raise LocadoraError(f"Filme '{self.titulo}' já está disponível")
        self.disponivel = True
        return self.calcular_multa()
    
    def calcular_multa(self):
        if self.data_emprestimo:
            dias_emprestimo = (datetime.now() - self.data_emprestimo).days
            if dias_emprestimo > 5:  # Prazo de 5 dias
                return (dias_emprestimo - 5) * 2.0  # R$ 2,00 por dia
        return 0.0
    
    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' - {self.diretor} [{status}]"

# CLASSE CLIENTE (Capítulo 7)
class Cliente:
    def __init__(self, nome: str, id_cliente: int):
        self.nome = nome
        self.id = id_cliente
        self.filmes_emprestados = []
    
    def pegar_emprestado(self, filme: Filme):
        if len(self.filmes_emprestados) >= 3:
            raise LimiteEmprestimosExcedidoError(
                f"Cliente {self.nome} excedeu o limite de 3 empréstimos"
            )
        
        filme.emprestar()
        self.filmes_emprestados.append(filme)
        return f"Filme '{filme.titulo}' emprestado com sucesso"
    
    def devolver_filme(self, filme: Filme):
        if filme not in self.filmes_emprestados:
            raise LocadoraError(f"Filme '{filme.titulo}' não foi emprestado por este cliente")
        
        multa = filme.devolver()
        self.filmes_emprestados.remove(filme)
        
        if multa > 0:
            return f"Filme devolvido com multa de R$ {multa:.2f}"
        return "Filme devolvido dentro do prazo"
    
    def __str__(self):
        filmes_titulos = [filme.titulo for filme in self.filmes_emprestados]
        return f"Cliente: {self.nome} (ID: {self.id}) - Filmes: {len(self.filmes_emprestados)} - {filmes_titulos}"

# EXEMPLO DE USO
if __name__ == "__main__":
    # Criando filmes e clientes
    filme1 = Filme("Interestelar", "Christopher Nolan", "001")
    filme2 = Filme("A Origem", "Christopher Nolan", "002")
    filme3 = Filme("Matrix", "Lana e Lilly Wachowski", "003")
    filme4 = Filme("O Senhor dos Anéis", "Peter Jackson", "004")
    
    cliente = Cliente("João Silva", 1)
    
    # Testando funcionalidades
    try:
        print("=== SISTEMA LOCADORA ===\n")
        print(cliente.pegar_emprestado(filme1))
        print(cliente.pegar_emprestado(filme2))
        print(cliente.pegar_emprestado(filme3))
        
        print(f"\nStatus do cliente: {cliente}")
        
        # Tentativa de pegar quarto filme (deve falhar)
        print("\nTentando pegar quarto filme...")
        print(cliente.pegar_emprestado(filme4))
        
    except (FilmeIndisponivelError, LimiteEmprestimosExcedidoError) as e:
        print(f"Erro: {e}")
    
    # Devolvendo filmes
    print("\n=== DEVOLUÇÃO DE FILMES ===")
    print(cliente.devolver_filme(filme1))
    print(f"Status após devolução: {filme1}")
    print(f"Status do cliente: {cliente}")
