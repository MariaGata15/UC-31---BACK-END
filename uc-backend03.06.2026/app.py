from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def cadastro():
    erros = []
    dados = {}

    if request.method == "POST":

        nome = request.form.get("nome", "").strip().title()
        email = request.form.get("email", "").strip().lower()
        telefone = request.form.get("telefone", "").strip()
        cpf = request.form.get("cpf", "").strip()
        cidade = request.form.get("cidade", "").strip().title()
        estado = request.form.get("estado", "").strip().upper()
        curso = request.form.get("curso", "").strip()
        idade = request.form.get("idade", "").strip()
        senha = request.form.get("senha", "").strip()

        telefone = (
            telefone.replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )

        cpf = cpf.replace(".", "").replace("-", "")

        # Validações
        if not nome:
            erros.append("Preencha todos os campos obrigatórios.")
        elif len(nome) < 8:
            erros.append("Nome inválido.")

        if not email or "@" not in email or ".com" not in email:
            erros.append("E-mail inválido.")

        if not telefone.isdigit() or len(telefone) != 11:
            erros.append("Telefone inválido.")

        if not cpf.isdigit() or len(cpf) != 11:
            erros.append("CPF inválido.")

        if not cidade or len(cidade) < 3:
            erros.append("Cidade inválida.")

        if not estado or len(estado) != 2 or not estado.isalpha():
            erros.append("Estado inválido.")

        if not curso:
            erros.append("Curso obrigatório.")

        if not idade.isdigit():
            erros.append("Idade inválida.")
        elif int(idade) < 16:
            erros.append("Idade mínima de 16 anos.")

        if len(senha) < 8 or not any(char.isdigit() for char in senha):
            erros.append("Senha muito fraca.")

        if not erros:
            dados = {
                "nome": nome,
                "email": email,
                "telefone": telefone,
                "cpf": cpf,
                "cidade": cidade,
                "estado": estado,
                "curso": curso,
                "idade": idade
            }

    return render_template(
        "index.html",
        erros=erros,
        dados=dados
    )

if __name__ == "__main__":
    app.run(debug=True)