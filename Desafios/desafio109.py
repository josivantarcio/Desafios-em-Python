import moeda
num = float(input('Digite um valor R$: '))
var = int(input('Variação: '))
print(f'O valor de {moeda.moeda(num)} com acrescimo de {var}% é igual a: {moeda.aumentar(num,var,True)}')
print(f'O valor de {moeda.moeda(num)} com desconto de {var}% é igual a: {moeda.diminuir(num,var,True)}')
print(f'O dobro de {moeda.moeda(num)} é igual a {moeda.dobro(num, True)}')
print(f'A metade de {moeda.moeda(num)} é igual a {moeda.metade(num,True)}')
print(f'O dízimo de {moeda.moeda(num)} é {moeda.dizimo(num,True)}')