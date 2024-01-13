from datetime import datetime as dt
class Pessoa:
    def __init__(self,nome:str,data_nascimento: str, peso: float, altura: float ) -> None:
        self.nome = nome
        self.data_nascimento = dt.strptime(self.data_nascimento, '%d/%m/%Y').date()
        self.peso = peso
        self.altura = altura
        self.calcular_idade()
        self.calcular_imc()
    
    def calcular_idade(self) -> None:
        data_atual = dt.now().date()
        self.idade = (data_atual - self.data_nascimento).days //365
    
    def calcular_imc(self) -> None:
        self.imc = self.peso/(self.altura**2)
        
    def __repr__(self) -> str:
        return f'Nome: {self.nome}, Data nascimento: {self.data_nascimento}, Peso: {self.peso}, Altura: {self.altura}, Idade: {self.idade}, IMC: {self.imc}'



        



        
        
        
        

