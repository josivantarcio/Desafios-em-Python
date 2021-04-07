numeros = list()
n = 0
while True:
    n = (int(input('Digite um valor: ')))

    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor ja existe!')

    stop = str(input('Deseja Continuar? ').strip().lower()[0])
    if stop == 'n':
        break
numeros.sort()
print(numeros)

