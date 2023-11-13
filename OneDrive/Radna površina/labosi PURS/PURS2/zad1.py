from flask import Flask,request,redirect,url_for,make_response

app = Flask("Prva Flask Aplikacija")

temperature = []

@app.get('/')
def index():
    return 'Početna stranica'

@app.get('/login')
def login():
    return 'Stranica za prijavu'

@app.post('/login')
def podaci():
    user = request.json.get('username')
    password = request.json.get('password')
    if user is not None and password is not None:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

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
    global temperatura
    json = {
        "temperatura":temperatura[-1]
    }
    resp = make_response(json, 202)
    return resp


if __name__ == '__main__':
    app.run(host= "0.0.0.0", port=80)


