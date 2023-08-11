'''Classe Pessoa: Crie uma classe que modele uma pessoa:Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.'''

class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def engordar(self, peso_ganho):
        self.peso += peso_ganho

    def emagrecer(self, peso_perdido):
        self.peso -= peso_perdido

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)

    def crescer(self, altura_ganha):
        self.altura += altura_ganha

nome = input('Digite o nome da pessoa: ')
idade = int(input('Digite a idade da pessoa: '))
peso = float(input('Digite o peso da pessoa: '))
altura = float(input('Digite a altura da pessoa: '))

pessoa = Pessoa(nome, idade, peso, altura)

print('Dados iniciais da pessoa:')
print('Nome:', pessoa.nome)
print('Idade:', pessoa.idade)
print('Peso:', pessoa.peso)
print('Altura:', pessoa.altura)