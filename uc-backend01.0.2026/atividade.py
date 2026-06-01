from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "senha_secreta"

@app.route("/", methods=["GET", "POST"])
def inscricao():
    if request.method == "POST":
        nickname = request.form.get("nickname")
        jogo = request.form.get("jogo")
        email = request.form.get("email")

        # Validações
        if not nickname or not jogo or not email:
            flash("Preencha todos os campos obrigatórios.", "erro")
            return redirect(url_for("inscricao"))

        if len(nickname) < 4:
            flash("Preencha todos os campos obrigatórios.", "erro")
            return redirect(url_for("inscricao"))

        flash("Inscrição realizada com sucesso!", "sucesso")
        return redirect(url_for("inscricao"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)