n1 = float(input('Digite nº1: '))
n2 = float(input('Digite nº2: '))
n3 = float(input('Digite nº3: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor= n3
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O Menor é {}'.format(menor))
print('O Maior é {}'.format(maior))