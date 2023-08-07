'''Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos 
atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu,
for informada na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.'''

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
 def getIdade(self):
  return self.idade
 def humor(self):
  return self.getFome() * self.getSaude()
 def alimenta(self, quantidade):
  if (quantidade >= 0) and (quantidade <= 100):
     self.fome -= self.fome * (quantidade /100.0)
 def brincar(self, quantidade):
  if (quantidade >= 0) and (quantidade <= 100):
     self.saude += self.saude * (quantidade / 100.0)
 def str(self):
    return ("Nome: " + str(self.getNome()) +", Fome:"+ "str"(self.getFome()) +"Saude:",+ str(self.getSaude())+"Idade:",+ str(self.getIdade()))
 
 
b = Bichinho("Tamagoshi", 5,5,5)
print(b.humor())
b.alimenta(30) 


print(b.humor())
b.brincar(20)
print(b.humor())
print(b.str())