from flask import Flask, render_template

app = Flask(__name__)

#QUESTÃO 1

@app.route('/arearestrita/<int:id>')
def arearestrita(id):
    if id == 1:
        return "CADEADO FECHADO"
    elif id == 2: 
        return "CADEADO ABERTO" 
    else: 
        return "ID INVALIDO"
    

#QUESTÃO 2 

@app.route('/operacao/<tipo>/<int:n1>/<int:n2>')
def operacao(tipo, n1, n2):
    if tipo == "sum":
        resultado = n1 + n2
    elif tipo == "sub":
        resultado = n1 - n2
    elif tipo == "mult":
        resultado = n1 * n2
    elif tipo == "div":
        if n2 == 0:
            return "ERRO: DIVISÃO POR ZERO"
        resultado = n1 / n2
    else:
        return "TIPO DE OPERAÇÃO INVÁLIDO"

    return str(resultado)

if __name__ == "__main__":
    app.run(debug=True)




