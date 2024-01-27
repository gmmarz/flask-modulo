def calcular_imc(pessoa_info: dict) -> float:
    peso = float(pessoa_info.get('peso'))
    altura = float(pessoa_info.get('altura'))
    imc = peso/(altura)**2
    return imc
    