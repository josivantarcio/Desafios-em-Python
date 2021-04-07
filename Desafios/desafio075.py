n = (int(input('Digite um valor: ')),
     int(input('Digite um valor: ')),
     int(input('Digite um valor: ')),
     int(input('Digite um valor: ')))

print('quantidade de Nove: ',n.count(9))
print('posicao do nr. 3: ',n.index(3))

for i in n:
    if i % 2 == 0:
        print(i, end=' ')
