class Escola():
    def __init__(self):
        self.alunos = []
        
    def cadastrar_aluno(self, nome):
        self.alunos.append(nome)
        
    def editar_aluno(self, nome_antigo, nome_novo):
        if nome_antigo in self.alunos:
            index = self.alunos.index(nome_antigo)
            self.alunos[index] = nome_novo
            print(f"Aluno {nome_antigo} editado para {nome_novo}.")
        else:
            print(f"Aluno {nome_antigo} não encontrado.")

    def excluir_aluno(self, nome):
        if nome in self.alunos:
            self.alunos.remove(nome)
            print(f"Aluno {nome} excluído.")
        else:
            print(f"Aluno {nome} não encontrado.")

    def mostrar_alunos(self):
        print("Alunos cadastrados:")
        for aluno in self.alunos:
            print(aluno)

# Criar instância da classe Escola
escola = Escola()

# Menu
while True:
    print("\nOpções:")
    print("1 - Cadastrar aluno")
    print("2 - Editar aluno")
    print("3 - Excluir aluno")
    print("4 - Mostrar alunos")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        escola.cadastrar_aluno(nome)
        print(f"Aluno {nome} cadastrado!")

    elif opcao == "2":
        nome_antigo = input("Digite o nome do aluno que deseja editar: ")
        nome_novo = input("Digite o novo nome do aluno: ")
        escola.editar_aluno(nome_antigo, nome_novo)

    elif opcao == "3":
        nome = input("Digite o nome do aluno que deseja excluir: ")
        escola.excluir_aluno(nome)

    elif opcao == "4":
        escola.mostrar_alunos()

    elif opcao == "0":
        print("Encerrando o programa. Até logo!")
        break

    else:
        print("Opção inválida. Escolha novamente.")







'''class Escola():
    def __init__(self):
       self.alunos = []
        
    
    
# menu
while True:
    print("\nOpções:")
    print("1 - cadastrar aluno")
    print("2 - editar aluno")
    print("3 - excluir aluno")
    print("4 - mostrar alunos")
    print("0 - sair")
    opcao = input("Escolha uma opção: ")
    

opcao = input("Escolha uma opção: ")
nome = str(input('Digite o nome da pessoa: '))
  return self.nome
editar_aluno = int(input('digite o nome da pessoa que deseja editar: '))
  return self.editar
excluir_aluno= str(input('Digite o nome pessoa que deseja excluir: '))
  return self.excluir
mostrar_mais= input("aluno deletado: ")
  return self.mostrar_mais
sair = input("sair: ")
  return self.sair
    
  if opcao == "1":
        print = int(input("digite o nome  do aluno: "))
        opcao.nome(nome)
        print(f"{self.alunos()} foi alimentado!")
   elif opcao == "2":
    quantidade = int(input("digite o nome que fgostaria de editar: "))
    bichinho.nome(nome)
    print(f"{bichinho.get_Nome()} o nome do aluno foi editado!")
   elif opcao == "3":
    print(f"aluno excluido, {self.alunos}!")


   elif opcao == "4":
    print(f"efetuando logoff...Adeus!, {alunos()}!")

   elif opcao == "0":
    print(f"Até logo, {self.alunos()}!")

     
else:
     print("Opção inválida. Escolha novamente.")'''