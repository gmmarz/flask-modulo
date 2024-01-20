from flask import Flask 

#criando nossa aplicação flask
app = Flask(__name__)
#Para inpedir o app de order as chaves do dicionario
app.json.sort_keys = False

#Aqui estamos criando uma rota
# @app.route('/')
# def hello_world():
#     return 'Hello World'
pessoas:list[dict] = [
    {
        "id":1,
        "nome":"Davi",
        "idade":30,
        "altura":1.7,
        "habilidades":["Python","flask","programação geral"]
    },
    {
        "id":2,
        "nome":"Gui",
        "idade":40,
        "altura":1.67,
        "habilidades":["Python","C#","alteryx","tableau"]
    },
    {
        "id":3,
        "nome":"Bi",
        "idade":40,
        "altura":1.65,
        "habilidades":["Empata","Sensitiva","gerenciamento"]
    },
]

# @app.route('/pessoas')
# def listar_pessoas():
#     return pessoas

#---------------------------
#Boas praticas informar quais metodos que a rota acita:
@app.route('/pessoas',methods = ['GET'])
def listar_pessoas():
    return pessoas

#Metodo para detelhar pessoas
#Isso chama path param - quando o parametro vem pela URL.
@app.route('/pessoas/<int:id>',methods = ['GET'])
def detalhar_pessoas(id:int):
    for pessoa in pessoas:
        if pessoa.get('id') == id:
            return pessoa
    return ({'message': 'Pessoa não encontrada'}, 404)

#Aqui estamos executando a aplicação

if __name__ == '__main__':
    app.run(debug=True)