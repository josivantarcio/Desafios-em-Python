pesoMaior = 0
pesoMenor = pesoMaior
for i in range(1, 6):
    peso = float(input('Digite o peso: '))
    if i == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso
print('O Maior peso: {}\nO Menor peso: {}'.format(pesoMaior, pesoMenor))