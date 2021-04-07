boletim = []
temp = []
while True:
    temp.clear()
    temp.append(str(input('Nome: ')).strip().title())
    temp.append(float(input('Nota 01: ')))
    temp.append(float(input('Nota 02: ')))
    stp = str(input('Deseja continuar? ').strip()[0].lower())
    boletim.append(temp[:])
    if stp in 'n':
        break
print('=' * 36)
print('             BOLETIM               ')
print('Nr  Nome        Média      Situação')
print('=' * 36)
for c, i in enumerate(boletim):
    for j in (boletim):
        media = (i[1] + i[2]) / 2
        if media >= 7:
            situacao = ('\033[1;32mAprovado\033[m')
        elif media < 7 and media >= 5:
            situacao = ('\033[1;33mRecuperação\033[m')
        elif media < 5:
            situacao = ('\033[1;31mReprovado\033[m')
    print(f'{c:<4}{i[0]:<12}{media:<11}{situacao:>10}')
while True:
    f = int(input('Deseja ver a nota de qual aluno? (999 p/ Sair)'))
    if f == 999:
        break
    if f <= len(boletim):
        print(f'As notas do aluno: {boletim[f][0]}, teve as notas {boletim[f][1]} e {boletim[f][2]}')