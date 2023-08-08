'''Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.'''

class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    
    def alterarValor(self, valorLitro):
        self.valorLitro = valorLitro
    
    def alterarCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel
    
    def alterarQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel
    
    def abastecerPorValor(self, valor):
        temp = valor / self.valorLitro
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - temp)
        return temp
    
    def abastecerPorLitro(self, qtd):
        temp2 = qtd * self.valorLitro
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - qtd)
        return temp2

# Exemplo de uso
bomba = BombaCombustivel("Gasolina", 5, 500)
print("Quantidade de combustível antes:", bomba.quantidadeCombustivel)

litros_abastecidos = bomba.abastecerPorValor(150)
print(f"Litros abastecidos: {litros_abastecidos}")
print("Quantidade de combustível após abastecimento:", bomba.quantidadeCombustivel)

valor_pago = bomba.abastecerPorLitro(30)
print(f"Valor pago: R${valor_pago}")
print("Quantidade de combustível após abastecimento:", bomba.quantidadeCombustivel)