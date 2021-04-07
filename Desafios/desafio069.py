somaIdade = somaHomem  = somaMulher = 0
while True:
    while True:
        idade = int(input('Digite a idade: '))
        if (idade > 0):
            break
    while True:
        sexo = str(input('Digite o Sexo M/F: ')).strip().upper()[0]
        if sexo in 'M' or sexo in 'F':
            break
    if(idade > 18):
        somaIdade += 1
    if(sexo in 'Mn'):
        somaHomem += 1
    if(sexo in 'Ff' and idade < 20):
        somaMulher += 1
    while True:
        i = str(input('Deseja continuar? ')).strip().lower()[0]
        if(i in 'Nn' or i in 'Ss'):
            break
    if(i in 'Nn'):
        break
print(f'{somaIdade} Pessoas com mais de 18 anos;\n'
      f'{somaHomem} Total de Homem cadastrado;\n'
      f'{somaMulher} Total de Mulher abaixo de 20 anos.')