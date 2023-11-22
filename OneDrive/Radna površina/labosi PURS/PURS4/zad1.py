from flask import Flask, request, redirect, url_for, make_response, render_template, session

app = Flask("Prva Flask Aplikacija")

temperature = []

app.secret_key = '_5#y2L"F4Q8z-n-xec]/'

@app.get('/')
def index():
    response = render_template('index.html')
    return response

@app.get('/login')
def login():
    response = render_template('login.html')
    return response

@app.post('/login')
def podaci():
    username = request.form.get('Username')
    password = request.form.get('Password')

    print(f"Username: {username}, Password: {password}")
    
    if username == 'PURS' and password == '1234':
        session['Username'] = username

        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.before_request
def before_request_func():
    if request.path == '/login':
        return 
    if session.get('Username') is None:
        return redirect(url_for('login'))

@app.get('/logout')
def logout():
    session.pop('Username')
    return redirect(url_for('index'))

@app.post('/temperatura')
def unos():
    global temperature
    temperatura = request.json.get('temperatura')
    if temperatura is not None:
        temperature.append(temperatura)
        return 'Uspješno ste postavili temperaturu', 201
    else:
        return 'Niste upisali ispravan ključ', 404

@app.get('/temperatura')
def provjera():
    global temperature
    json = {
        "temperatura": temperature[-1]
    }
    resp = make_response(json, 202)
    return resp

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
