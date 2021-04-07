cont = 0
acomulador = 0
n = 0
n = int(input('Digite um numero '))
while n != 999:
    cont += 1
    acomulador += n
    n = int(input('Digite um numero '))
print('Quantidade: {}\nSoma: {}'. format(cont, acomulador))
