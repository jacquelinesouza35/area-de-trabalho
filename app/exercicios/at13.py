'''Classe Funcionário: Implemente a classe Funcionário.
Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário)
e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.'''

class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def getNome(self):
        return self.nome
    
    def getSalario(self):
        return self.salario

# Teste da classe Funcionario
Func = Funcionario("Jose", 1200)
print("Nome:", Func.getNome(), ", Salario:", Func.getSalario())