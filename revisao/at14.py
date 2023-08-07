'''Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)'''

class Funcionario():
 def __init__(self, nome, salario):
  self.nome = nome
  self.salario = salario
 def getNome(self):
  return self.nome
 def getSalario(self):
  return self.salario
 def aumentarSalario(self, porcentagemDeAumento=0):
  self.salario += self.salario * (porcentagemDeAumento)/100
Func = Funcionario("Jose", 1200)
print("Nome: ", Func.getNome(), ", Salario", Func.getSalario())
Func.aumentarSalario(10)
print("Nome: ", Func.getNome(), ", Salario", Func.getSalario()) 