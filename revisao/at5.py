'''Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta,
nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.'''

class Conta():
 def __init__(self, numero, nome, saldo=0):
  self.numero = numero
  self.nome = nome
  self.saldo = saldo
 def setNome(self, nome):
  self.nome = nome
 def deposito(self, valor):
  self.saldo += valor
 def saque(self, valor):
   if (self.saldo >= valor):
    self.saldo -= valor
 
j = Conta(123, "José", 100.0)
print(vars(j))
j.setNome("Pedro")
j.deposito(50)
print(vars(j))
j.saque(110)
print(vars(j))