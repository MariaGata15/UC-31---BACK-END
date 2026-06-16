from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'chave-secreta-super-segura'

USUARIO_VALIDO = 'admin'
SENHA_VALIDA = '12345'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        
    
        if usuario == USUARIO_VALIDO and senha == SENHA_VALIDA:
            session['usuario'] = usuario 
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuário ou senha inválidos.', 'danger')
            
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        flash('Por favor, faça login para acessar esta página.', 'warning')
        return redirect(url_for('login'))
        
    return render_template('dashboard.html', usuario=session['usuario'])

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
