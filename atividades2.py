from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return 'OLAAAAAAAAA'


#ATIVIDADE 2

#QUESTÃO1 

@app.route('/ola/<nome>')
def ola(nome):
    nome= "Rivia"
    return  f"Ola, {nome}! Seja bem-vinda ao sistema"


#QUESTÃO2 

@app.route('/calculo/<int:n1>/<int:n2>')
def calculo(n1, n2):
    resultado = n1 + n2
    return f"A soma de {n1} +{n2} é {resultado}"

#QUESTÃO4 

@app.route('/produto/<nome>/<float:preco>')
def produto(nome, preco):
    return f"O produto {nome} custa R$ {preco:.2f}"

if __name__ == "__main__":
    app.run(debug=True)