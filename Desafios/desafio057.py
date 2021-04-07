sexo = str(input('Sexo M/F: ')).strip().upper()
while sexo not in 'MmFf':
    print('Valor errado, favor digitar novamente!')
    sexo = str(input('Sexo M/F: ')).strip().upper()
print('Sexo = {}'.format(sexo))