from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"

@app.route("/")
def inicio():
    return """
    <h1>Página Inicial</h1>
    <a href="/contador">Ir para Contador</a>
    """


@app.route("/contador")
def contador():
    # contador de acessos (implementação auxiliada por IA)
    
    if "contador" not in session:
        session["contador"] = 0

    session["contador"] += 1

    return render_template(
        "contador.html",
        acessos=session["contador"]
    )


@app.route("/zerar")
def zerar():
    session.pop("contador", None)  # remove apenas o contador
    return redirect(url_for("contador"))


if __name__ == "__main__":
    app.run(debug=True)