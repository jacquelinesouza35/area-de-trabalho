'''Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;'''


class Quadrado():
    def __init__(self, lado):
        self.setLado(lado)
    
    def setLado(self, lado):
        self.lado = lado
    
    def getLado(self):
        return self.lado
    
    def area(self):
        return self.lado * self.lado

q = Quadrado(8)
print(q.area())