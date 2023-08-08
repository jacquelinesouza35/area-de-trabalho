'''Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. 
Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira.
Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos).
Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.
'''
from random import randint

class Bichinho():
    def __init__(self, nome, fome, saude, idade):
        self.set_Nome(nome)
        self.set_Fome(fome)
        self.set_Saude(saude)
        self.set_Idade(idade)

    def set_Nome(self, nome):
        self.nome = nome
    def set_Fome(self, fome):
        self.fome = fome
    def set_Saude(self, saude):
        self.saude = saude
    def set_Idade(self, idade):
        self.idade = idade
    def get_Nome(self):
        return self.nome
    def get_Fome(self):
        return self.fome
    def get_Saude(self):
        return self.saude
    def get_Idade(self):
        return self.idade
    def humor(self):
        return self.get_Fome() * self.get_Saude()
    def alimenta(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 100.0)
    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.saude += self.saude * (quantidade / 100.0)

# Criar um bichinho virtual
nome = input("Digite o nome do seu bichinho: ")
bichinho = Bichinho(nome, randint(1, 100), randint(1, 100), randint(1, 10))

# Interagir com o bichinho
while True:
    print("\nOpções:")
    print("1 - Alimentar")
    print("2 - Brincar")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        quantidade = int(input("Digite a quantidade de alimento (0-100): "))
        bichinho.alimenta(quantidade)
        print(f"{bichinho.get_Nome()} foi alimentado!")

    elif opcao == "2":
        quantidade = int(input("Digite a quantidade de brincadeira (0-100): "))
        bichinho.brincar(quantidade)
        print(f"{bichinho.get_Nome()} brincou e está mais saudável!")

    elif opcao == "3":
        print(f"Até logo, {bichinho.get_Nome()}!")
        break

    else:
        print("Opção inválida. Escolha novamente.")