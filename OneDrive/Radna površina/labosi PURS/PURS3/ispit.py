from flask import Flask,request,render_template,url_for,redirect 

app = Flask("Prva Flask aplikacija")

@app.get('/pocetna_stranica')
def ispit():
    return render_template('ispit.html')

@app.post('/korisnicki_unos')
def provjera():
    text = request.form('text')
    password = request.form('password')
    email = request.form('email')

    if text and password and email is not None:
        return redirect(url_for('/pocetna_stranica'))
    else:
        return redirect(url_for('/pocetna_stranica'))


if __name__ == '__main__':
    app.run(host= "0.0.0.0", port=80)


