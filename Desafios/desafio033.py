n1 = float(input('Digite nº1: '))
n2 = float(input('Digite nº2: '))
n3 = float(input('Digite nº3: '))
# if(n1 > n2 and n1 > n3):
#     print('{} é o maior'.format(n1))
# elif(n3 > n2 and n3 > n1):
#     print('{} é o maior'.format(n3))
# else:
#     print('{} é o maior'.format(n2))
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
