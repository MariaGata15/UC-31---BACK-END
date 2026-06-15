from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "segredo123"

# Produtos simulados
produtos = [
    {"id": 1, "nome": "Notebook"},
    {"id": 2, "nome": "Mouse"},
    {"id": 3, "nome": "Teclado"},
    {"id": 4, "nome": "Monitor"},
    {"id": 5, "nome": "Celular"}
]


@app.route("/")
def inicio():
    favoritos = session.get("favoritos", [])
    return render_template(
        "index.html",
        produtos=produtos,
        favoritos=favoritos
    )


@app.route("/favoritar/<int:id>")
def favoritar(id):

    if "favoritos" not in session:
        session["favoritos"] = []

    if id not in session["favoritos"]:
        session["favoritos"].append(id)
        session.modified = True

    return redirect(url_for("inicio"))


@app.route("/favoritos")
def favoritos():

    ids = session.get("favoritos", [])

    lista = []

    for produto in produtos:
        if produto["id"] in ids:
            lista.append(produto)

    return render_template(
        "favoritos.html",
        favoritos=lista
    )


@app.route("/remover/<int:id>")
def remover(id):

    if "favoritos" in session:

        if id in session["favoritos"]:
            session["favoritos"].remove(id)
            session.modified = True

    return redirect(url_for("favoritos"))


if __name__ == "__main__":
    app.run(debug=True)