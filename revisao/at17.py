'''Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. 
Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira.
Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos).
Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.
'''

from random import randint
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
   if(quantidade >= 0) and (quantidade <= 100):
    self.fome -= self.fome * (quantidade /100.0)
 def brincar(self, quantidade):
    if(quantidade >= 0) and (quantidade <= 100):
        self.saude >= self.saude * (quantidade / 100.0)