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
        print(f"Bucho do {self.nome}: {self.bucho}")
    
    def digerir(self):
        if len(self.bucho) > 0:
            self.bucho.pop(0)

# Criando dois macacos
m1 = Macaco("Macaco 1")
m2 = Macaco("Macaco 2")

# Alimentando o primeiro macaco
m1.comer("Maçã")
m1.comer("Banana")
m1.comer("Abacaxi")

# Verificando o bucho do primeiro macaco
m1.verBucho()

# Digerindo alimentos do primeiro macaco
m1.digerir()
m1.verBucho()

# Alimentando o segundo macaco
m2.comer("Maca")
m2.comer("Banana")
m2.comer(m1)  # O segundo macaco "come" o primeiro

# Verificando o bucho do segundo macaco
m2.verBucho()