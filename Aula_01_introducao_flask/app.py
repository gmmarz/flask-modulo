from flask import Flask 

#criando nossa aplicação flask
app = Flask(__name__)

#Aqui estamos criando uma rota
@app.route('/')
def hello_world():
    return 'Hello World'

#Aqui estamos executando a aplicação

if __name__ == '__main__':
    app.run(debug=True)