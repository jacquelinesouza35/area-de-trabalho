
#Possua uma classe chamada Retangulo, com os atributos largura e altura.Possua uma função para imprimir os valores da classe Ponto
#Possua uma função para encontrar o centro de um Retângulo.Você deve criar alguns objetos da classe Retangulo.Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do 
#retângulo, que deve ser um objeto da classe Ponto.A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto
#que indique os valores de x e y para o centro do objeto.
#o valor do centro do objeto deve ser mostrado na tela Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto:
 def __init__(self, x, y):
     self.x = x
 self.y = y
class Retangulo:
 def __init__(self, canto1, canto2):
     self.canto1 = canto1
 self.canto2 = canto2
 def centro(self):
x_centro = (self.canto1.x + self.canto2.x) / 2.0
y_centro = (self.canto1.y + self.canto2.y) / 2.0
 return "X=" + str(x_centro) + "Y=" + str(y_centro)
x1 = float(input("Entre a coordenada x do canto inferior esquerdo: "))
y1 = float(input("Entre a coordenada y do canto inferior esquerdo: "))
canto1 = Ponto(x1, y1)
x2 = float(input("Entre a coordenada x do canto superior direito: "))
y2 = float(input("Entre a coordenada y do canto superior direito: "))
canto2 = Ponto(x2, y2)
ret = Retangulo(canto1, canto2)
print ("Ponto central e %s" % ret.centro())