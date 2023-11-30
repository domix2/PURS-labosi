from flask import Flask, request, redirect, url_for, make_response, render_template, session

app = Flask("Prva Flask Aplikacija")

temperature = temperature_data = [
    {"datum": "Datum 1", "vrijednost": 23},
    {"datum": "Datum 2", "vrijednost": 23},
    {"datum": "Datum 3", "vrijednost": 23},
    {"datum": "Datum 4", "vrijednost": 23},
]
list = [
    {"datum": "Datum 1", "vrijednost": 50},
    {"datum": "Datum 2", "vrijednost": 55},
    {"datum": "Datum 3", "vrijednost": 60},
    {"datum": "Datum 4", "vrijednost": 65},
]

app.secret_key = '_5#y2L"F4Q8z-n-xec]/'

@app.get('/')
def index():
    tip_podataka = request.args.get('id', '1')  

    if tip_podataka == '1':
        podaci = temperature
        naslov_stupca = 'Temperatura'
    elif tip_podataka == '2':
        podaci = list
        naslov_stupca = 'Vlaga zraka'
    else:
        return redirect(url_for('index', id='1'))  # Ako id nije 1 ili 2, preusmjeri na listu temperatura

    naslov_stupca = 'Temperatura' if tip_podataka == '1' else 'Vlaga zraka'

    return render_template('index.html', title='Main Page', Username=session.get('Username', '').capitalize(), podaci=podaci, naslov_stupca=naslov_stupca)

@app.get('/login')
def login():
    poruka=None
    response = render_template('login.html', title='Prijava',poruka=poruka)
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
        return render_template('login.html',poruka= 'Uneseni su pogrešni podaci')

@app.before_request
def before_request_func():

    # Ignore authorization check for static folder / GET static content
    if request.path.startswith('/static'):
        return
    
    # If user is not authorized and request path is not login
    if session.get('Username') is None and request.path != '/login' :
        return redirect(url_for('login')) # Return login page
    elif session.get('Username') is not None and request.path == '/login': # User is authorized and login page is requested
        return redirect(url_for('index')) # Return home page

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
