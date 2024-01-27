from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def somar():
    # data: dict = request.form.copy()
    # numero1 = float(data.get('num-1'))
    # numero1 = data.get('')
    #Como o html não pode enviar vazio podemos pegar direto
    numero1 = float(request.form.get('num-1'))
    numero2 = float(request.form.get('num-2'))
    resultado = numero1 + numero2
    return render_template('index.html',soma=resultado)


if __name__ == '__main__':
    app.run(debug=True)
