from flask import Flask, render_template

app = Flask(__name__)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    nome = "Clara*"
    return render_template('index.html', title='Página Inicial', nome=nome)
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    nome= "Clara"
    return render_template('contato.html', title = 'Pagina Inicial', nome=nome)

@app.route("/contato")
def contato():
    return "Pagina de Contato"

#04/05 - AULA

@app.route('/')
@app.route('contato')
def contato():
    return render_template('contato.html', usuario=None, nome=None, title='Home')

@app.route ('/usuario')
def usuario():
    usuario = {'nome': 'Clara','email': 'mariaclarashinbel2021@gmail.com'}
    return render_template('contato.html', title = 'Pagina Inicial', usuario=usuario, nome=None)

# 05/05 - AULA

@app.route('/dados', defaults ={"nome":"usuario comum"})
@app.route('/dados/<nome>')
def dados(nome):
    return f'Olá, {nome}!'

@app.route('/semestre/<int:x>')
def semestre(x):
    return 'Estamos no semestre' + str(x)

@app.route('/pagamento/<float:valor>')
def pagamento (valor):
    return 'Você pagou: '+str(valor)

@app.route('/somar', defautlts={"n1": "0", "n2": "0"})
@app.route('/somar/<int:n1>/<int:n2>')
def somar(n1, n2):
    resultado = n1 + n2
    return str(resultado)

@app.route('/soma', defautlts={"n1": "0", "n2": "0"})
@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1, n2):
     resultado = n1 + n2
     return render_template('contato.html', n1=n1, n2=n2, resultado=resultado)

@app.route('/arearestrita/<int:id>')
def arearestrita(id):
    if id == 1:
        return "Acesso bloqueado (cadeado fechado)"
    else: 
        return "Acesso liberado (cadeado aberto)" 


if __name__ == "__main__":
    app.run(debug=True)

@app.route('/contato')
def contato():
    return 'Página de contato'

if __name__ == '__main__':
    app.run()
    



