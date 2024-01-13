#Revisao de dicionario
#MANIPULACAO DE DICIONARIO É A PARTE MUITO IMPORTANTE PARA O FLASK
#funcao "dir" para listar listar metodos
aluno = {
    'nome':'carlos',
    'idade':20,
    'notas':[6,5,7],
    'media':6,
    'ativo':True
}

# #Buscando uma chave do dicionario
# #Caso buscar uma chave que não exista neste caso ele quebra o código, parando a execução
# print(aluno['nome'])
# print(aluno['notas'])
# # print(aluno['qualquer'])

# #recomendado, é não pegar os valores utilizando o nome da chave diretamente, mas sim utilizar a função get, pois ela não quebra o codigo
# print(aluno.get('nome'))
# print(aluno.get('qualquer',False))

#Exemplo de utilização do update para autalizar um dicionário
#A vantagem do update é que dá a posibilidade de adicionar ou alterar multiplas chaves e valores
print(aluno)

aluno.update({'nome':'Laura','presenca':1})
print(aluno)

#Uma maneira interessante de imprimir um dicionario ( desmpacotar o dicionario)
for key,value in aluno.items():
    print(f'{key}:{value}')