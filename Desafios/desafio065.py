sinal = 's'
cont = 0
acomulador = 0
while sinal not in 'Nn':
    n = int(input('Digite um valor: '))
    acomulador += n
    cont += 1
    if cont == 1:
        nMaior = nMenor = n
    else:
        if n > nMaior:
            nMaior = n
        if n < nMenor:
            nMenor = n
    sinal = str(input('Quer continuar? '))
media = acomulador / cont
print(f'O Total foi de {acomulador}\nA Média de {cont} foi de {media:.2f}\n'
      f'E o maior número foi: {nMaior}\nE o menor número foi: {nMenor}')