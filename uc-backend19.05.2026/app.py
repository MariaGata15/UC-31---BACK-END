from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():

    lanches = [
        {
            'nome': 'Pastel de Frango',
            'descricao': 'Pastel recheado com frango e queijo.',
            'preco': '12,00',
            'imagem': 'pastel.jpg'
        },

        {
            'nome': 'Cachorro Quente',
            'descricao': 'Cachorro quente completo e saboroso.',
            'preco': '14,00',
            'imagem': 'cachorro.jpg'
        },

        {
            'nome': 'Milkshake',
            'descricao': 'Milkshake cremoso de chocolate.',
            'preco': '16,00',
            'imagem': 'milkshake.jpg'
        },

        {
            'nome': 'Batata Frita',
            'descricao': 'Batata frita crocante.',
            'preco': '15,00',
            'imagem': 'batata.jpg'
        },

        {
            'nome': 'Hambúrguer',
            'descricao': 'Hambúrguer artesanal com queijo.',
            'preco': '18,00',
            'imagem': 'hamburguer.jpg'
        }
    ]

    return render_template('cardapio.html', lanches=lanches)

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/cliente/<nome>')
def cliente(nome):
    return render_template('cliente.html', nome=nome)

@app.route('/lanche/<item>')
def lanche(item):
    return render_template('lanche.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)