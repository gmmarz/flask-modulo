class Produto:
    def __init__(self,nome:str,categoria:str,preco:float,desconto:int = 0) -> None:
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.desconto = desconto
    
    def applicar_desconto(self) -> None:
        self.preco = self.preco * ((100 - self.desconto)/100)
    
produto1 = Produto('Cafe','cafe',3)
produto2 = Produto('Picanha','Carne',45,10)

print(f'Preco antes do desconte:{produto2.preco}')
produto2.applicar_desconto()
print(f'Preco depois do desconto: {produto2.preco}')