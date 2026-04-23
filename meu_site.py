from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)

relatos = []

@app.route('/')
def inicio ():
    return redirect(url_for('login'))

@app.route('/homepage')
def homepage():
    return render_template("homepage.html")


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        conn = sqlite3.connect('site.db')
        cursor = conn.cursor()

        cursor.execute(
            'SELECT * FROM usuario WHERE usuario=? AND senha=?',
            (usuario, senha)
        )
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            return redirect(url_for('homepage'))
        else:
            return 'usuário ou senha incorretos!'

    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        conn = sqlite3.connect('site.db')
        cursor = conn.cursor()

        cursor.execute(
            'iNSERT INTO usuario (usuario, senha) VALUES (?,?)',
            (usuario,senha)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('homepage'))
    return render_template('cadastro.html')

@app.route('/relatos', methods=['GET', 'POST'])
def relatos():
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        texto = request.form.get('relato')
        if texto and texto.strip() != "":
            anonimo = request.form.get('anonimo', 'nao')
            nome = "Anônimo" if anonimo == "sim" else request.form.get('nome', 'Desconhecido')

            cursor.execute(
            'INSERT INTO relatos (texto, nome) VALUES (?, ?)',
            (texto, nome)
            )
            conn.commit()
            print('Relato salvo:', texto)

        conn.close()
        return redirect(url_for('relatos'))

    cursor.execute('SELECT nome, texto FROM relatos')
    lista_relatos = cursor.fetchall()
    conn.close()
    return render_template('relatos.html', relatos=lista_relatos)

@app.route('/seguranca')
def seguranca():
    return render_template('seguranca.html')


@app.route('/relacionamento')
def relacionamento():
    return render_template('relacionamento.html')

    if __name__ == "__main__":
        app.run(debug=True)

@app.route('/definicao')
def definicao():
    return render_template('definicao.html')


@app.route('/emergencia')
def emergencia():
    return render_template('emergencia.html')


if __name__ == "__main__":
    app.run(debug=True)
