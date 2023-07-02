from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = b'85e712445fd4b29012ea392d0ee32dbd3cfea64fd0c5d4264ce2e1e98f248c11'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/square/', methods=['GET','POST'])
def square():
    if request.method == 'POST':
        number = int(request.form.get('num'))
        return f'Введено число {number}, квадрат числа равен {number ** 2}.'
    return render_template('square.html')


@app.route('/hello/')
def hello():
    return render_template('hello.html', username = session['username'])


@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        session['email'] = request.form.get('email')
        return redirect(url_for('hello'))
    return render_template('form.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)