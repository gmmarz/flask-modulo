from flask import Flask, render_template, request
# from utilities_func import calcular_imc

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def calcular_imc():
    data: dict = request.form.copy()
    peso = float(request.form.get('peso1'))
    altura = float(request.form.get('altura1'))
    imc = peso/altura**2
    if imc < 18.5:
        cat = 'Abaixo peso'
    elif imc <30:
        cat = 'Sobrepreso'
    elif imc <35:
        cat = 'Obesidade I'
    elif imc <40:
        cat = 'Obesidade II'
    else:
        cat = 'Obesidade III'
    
    context = {'imc': round(imc,2),'categoria':cat}
    return render_template('index.html',**context)

if __name__ == '__main__':
    app.run(debug=True)