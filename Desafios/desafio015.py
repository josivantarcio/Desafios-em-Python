km = float(input('Quantidade de KM? '))
km = km * 0.15
d = int(input('Quantidade de dias? '))
d = d * 60.00
valor = km + d
print('Valor a Pagar R${:.2f}'.format(valor))
