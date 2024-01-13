#Revisao sobre listas
nome = 'erik'
nome = 'samuel'
#Mostra uma variável sobreescrevendo

#Variáveis compostas| listas| Arrays | vetores
#Boa pratica para nomear listas - utilizar palavras no plural
nomes = ['Duke']
nomes.append('Guilherme')
nomes.insert(0,'Lucas')
nomes.pop(1)
print(nomes)
#Iterável é uma palavra para varrer um vetor

#exemplo de mostrar dados de uma lista utilizando enumerete
linguagens = ['ingles','portugues','frances']
for indice,lingua in enumerate(linguagens,start= 1):
    print(f'{indice}º {lingua}')
    