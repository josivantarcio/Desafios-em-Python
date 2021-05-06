#Um melhor desenvolvimento deste exercício, está no desafio109.py
from utilidadesCeV import moeda
num = float(input('Digite um valor R$: '))
var = int(input('Variação: '))
print(f'O valor de {moeda.moeda(num)} com acrescimo de {var}% é igual a: {moeda.moeda(moeda.aumentar(num,var))}')
print(f'O valor de {moeda.moeda(num)} com desconto de {var}% é igual a: {moeda.moeda(moeda.diminuir(num,var))}')
print(f'O dobro de {moeda.moeda(num)} é igual a {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é igual a {moeda.moeda(moeda.metade(num))}')
print(f'O dízimo de {moeda.moeda(num)} é {moeda.moeda(moeda.dizimo(num))}')