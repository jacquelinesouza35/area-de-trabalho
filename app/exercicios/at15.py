'''Classe Bichinho Virtual++: Melhore o programa do bichinho virtual,
permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho.
Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.'''


class Bichinho():
 def __init__(self, nome, fome, saude, idade):
  self.setNome(nome)
  self.setFome(fome)
  self.setSaude(saude)
  self.setIdade(idade)
 def setNome(self, nome):
  self.nome = nome 
 def setFome(self, fome):
  self.fome = fome
 def setSaude(self, saude):
  self.saude = saude
 def setIdade(self, idade):
  self.idade = idade
 def getNome(self):
  return self.nome
 def getFome(self):
  return self.fome
 def getSaude(self):
  return self.saude
 def getIdade(self, idade):
  return self.idade
 def humor(self):
  return self.getFome() * self.getSaude()
 
b = Bichinho("Tamagoshi", 5,5,5)
print(b.humor())