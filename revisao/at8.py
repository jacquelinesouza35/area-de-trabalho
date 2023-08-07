'''Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos,
alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.
Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?'''

class Macaco():
 def __init__(self, nome):
  self.nome = nome
  self.bucho = []
 def comer(self, comida):
    self.bucho.append(comida)
 def verBucho(self):
  print ("Bucho: " , self.bucho)
 def digerir(self):
  if (len(self.bucho) > 0):
    self.bucho.pop(0)
m1 = Macaco("Macaco 1")
m2 = Macaco("Macaco 2")
m1.comer("Maçã")
m1.verBucho()
m1.comer("Banana")
m1.verBucho()
m1.comer("Abacaxi")
m1.verBucho()
m1.digerir()
m1.verBucho()
m2.comer("Maca")
m2.comer("Banana")
m2.comer(m1)
m2.verBucho()