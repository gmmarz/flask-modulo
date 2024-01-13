#Sempre bom utilizar type hint. 
#é possível passar um valor padrão.
def inverter_texto(texto: str = 'abcdh') -> str:
    return texto[::-1]