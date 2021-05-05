#Um melhor desenvolvimento deste exercício, está no desafio108.py
import moeda
num = float(input('Digite um valor R$: '))
var = int(input('Variação: '))
print(f'O valor {num} com acrescimo de {var}% é {moeda.aumentar(num, var)}')
print(f'O valor {num} com desconto de {var}% é {moeda.diminuir(num, var)}')
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')