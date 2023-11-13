from flask import Flask,request 

app = Flask("Prva Flask aplikacija")

@app.get('/jos_malo_pa_gotovo')
def brzo():
    moji_bodovi = {'moji_bodovi': 3}
    return moji_bodovi, 201

@app.get('/putanja_get')
def put():
    print(request.args.get('hocu_bodove'))
    return 'samo_jako'


@app.post('/hocu_sve_bodove')
def postavi():
    svi_bodovi = request.json.get('svi bodovi')
    if svi_bodovi is not None:
        return 'moji_bodovi'

if __name__ == '__main__':
    app.run(host= "0.0.0.0", port=80)