from datetime import datetime as dt

# def calcular_idade(data_nascimento):
#     data_atual = dt.now().date()
#     data_nascimento = dt.strptime(data_nascimento, '%d/%m/%Y').date()
#     idade = (data_atual - data_nascimento).days //365
#     return idade
    
   
# nascimento = "25/09/1982"
# idade = calcular_idade(nascimento)

# print(f"Idade é {idade}")

# ano_now = dt.now().date().year

# print(ano_now)

def test_tupla() -> tuple:
    return (-1,"teste")


flg,nome = test_tupla()

print(f'flg = {flg}, nome = {nome}')