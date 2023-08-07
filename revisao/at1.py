'''Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor'''


class Bola():
 def __init__(self, cor, circunferencia, material):
  self.cor = cor
  self.circunferencia = circunferencia
  self.material = material
 def trocaCor(self, cor):
  self.cor = cor
 def mostraCor(self):
  return self.cor
b = Bola("azul", 10, "couro")
print(b.mostraCor())
b.trocaCor("vermelha")
print(b.mostraCor())