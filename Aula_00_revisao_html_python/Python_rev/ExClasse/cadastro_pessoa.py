from cls_Pessoa import Pessoa
from datetime import datetime as dt

def requisitar_nome() -> tuple:
    nome = input("Digitar seu nome: ")
    resultado = ""
    if len(nome) <= 2:
        resultado = (-1,"Nome deve conter mais de 2 caracteres")
    else:
        resultado = (1,nome)
    return resultado

def requisitar_data_nascimento() -> tuple:
    in_data = {}
    print("Data nascimento:")    
    #Requisitando mes
    try:
        mes = int(input("Digite o número do mês: "))
        if mes > 12:
            return (-1, "Erro na data")
        else:
            in_data.update({"mes":mes})
    except ValueError:
        return (-1, "Erro na data")

    #requisitando dia
    try:
        dia = int(input("dia: "))
        if in_data.get('mes') in [1,3,5,7,8,10,12] and dia > 31 or dia < 1:
            return (-1, "Erro na data")
        elif in_data.get('mes') in [4,6,9,11] and dia > 30:
            return (-1, "Erro na data")
        elif in_data.get('mes') == 2 and dia > 29:
            return (-1, "Erro na data")
        else:
            in_data.update({'dia':dia}) 
    except ValueError:
        return (-1, "Erro na data")

    #Requisitando o ano
    try:
        ano = int(input("Ano 4 digitos: "))
        ano_now = dt.now().date().year
        if ano_now - ano < 0 or ano_now - ano > 120:
            return (-1, "Erro na data")
        else:
            in_data.update({"ano":ano})
    except ValueError:
        return (-1, "Erro na data")
    
    return (1,f"{in_data['dia']}/{in_data['mes']}/{in_data['ano']}")

def requisitar_peso() -> tuple:
    try:
        peso = float(input("Digite peso: "))
    except ValueError:
        return (-1,"Erro peso")
    return (1,peso)

def requisitar_altura() -> tuple:
    try:
        altura = float(input("Digite altura: "))
    except ValueError:
        return (-1,"Erro altura")
    return (1,altura)

def cadastrar_pessoas(pessoas:list) -> tuple:
    flg_cadastro = True

    while flg_cadastro:
        flg_err, nome  = requisitar_nome()
        if flg_err == -1:
            op = input("Erro no nome, deseja retornar s = sim , n = não")
            if op == "n":
                resultado = (-1,"Operação abortada")
                return resultado
        else:
            flg_err, data_nascimento = requisitar_data_nascimento()
            if flg_err == -1:
                op = input("Erro no nome, deseja retornar s = sim , n = não")
                if op == "n":
                    resultado = (-1,"Operação abortada")
                    return resultado
            else:
                flg_err,peso = requisitar_peso()
                if flg_err == -1:
                    op = input("Erro no nome, deseja retornar s = sim , n = não")
                    if op == "n":
                        resultado = (-1,"Operação abortada")
                        return resultado
                else:
                    flg_err,altura = requisitar_altura()
                    if flg_err == -1:
                        op = input("Erro no nome, deseja retornar s = sim , n = não")
                        if op == "n":
                          resultado = (-1,"Operação abortada")
                          return resultado
                    else:
                        pessoa = Pessoa(nome,data_nascimento,peso,altura)
                        pessoas.append(pessoa)
                        op = input("Deseja cadastrar outra pessoa: s = sim, n = não")
                        if op == "n":
                            flg_cadastro = False
    return (1,pessoas)                            

def mostrar_pessoas(pessoas: list) -> None:
    for pessoa in pessoas:
        print(pessoa)
            



flg_app = True

pessoas = []

while flg_app:
    try:
        print("Digite uma das opções:\
              \n1: Cadastrar novas pessoas\
              \n2: Mostrar pessoas cadastradas\
              \n3: Interromper programa")
        op = int(input("Digite a op desejado:"))
        match op:
            case 1:
                flg,pessoas_tmp = cadastrar_pessoas(pessoas)
                if flg == -1:
                    print(f"Error", pessoas_tmp)
                else:
                    pessoas = pessoas_tmp
            case 2:
                mostrar_pessoas(pessoas)
            case 3:
                print("Programa interrompido")
                break
            case _:
                print("Digite apenas as opções mostrada")

    except ValueError:
        print("Digite apenas as opções mostrada")

