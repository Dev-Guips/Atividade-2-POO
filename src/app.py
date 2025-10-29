from flask import Flask, render_template, request, redirect, url_for
from locadora import Locadora, Filme

app = Flask(__name__)

locadora = Locadora()

# --- adicionar filmes iniciais ao catálogo ---
def inicializar_catalogo():
    filmes_iniciais = [
        Filme("Interestelar", "Sci-Fi", "Christopher Nolan", 1, 2014, 169, 5),
        Filme("Matrix", "Sci-Fi", "Wachowski", 2, 1999, 136, 3),
        Filme("Toy Story", "Animação", "John Lasseter", 3, 1995, 81, 2)
    ]
    for f in filmes_iniciais:
        if f.id_filme not in locadora.catalogo:
            locadora.adicionar_filme(f)

inicializar_catalogo()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/filmes")
def filmes():
    filmes = locadora.catalogo.values()
    return render_template("filmes.html", filmes=filmes)

@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form["nome"]
        genero = request.form["genero"]
        autor = request.form["autor"]
        id_filme = int(request.form["id_filme"])
        ano = int(request.form["ano"])
        duracao = int(request.form["duracao"])
        qtd = int(request.form["qtd"])

        novo = Filme(nome, genero, autor, id_filme, ano, duracao, qtd)
        locadora.adicionar_filme(novo)

        return redirect(url_for('filmes'))

    return render_template("cadastrar_filme.html")

if __name__ == "__main__":
    app.run(debug=True)
