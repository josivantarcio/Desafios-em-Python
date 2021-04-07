from math import hypot
ca = float(input('Valor do Cateto adjacente: '))
co = float(input('Valor do Cateto Oposto: '))
hi = hypot(ca,co)
print('A Hipotenusa é: {:.2f}'.format(hi))