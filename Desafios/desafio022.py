nome = (input('Digite nome completo '))
print('Maiusculo: {}'.format(nome.upper()))
print('Minusculo: {}'.format(nome.lower()))

nomeQuebrado = nome.split()
nome = '.'.join(nomeQuebrado)
i = len(nome)
j = nome.count('.')
print('quantidade de caracteres {} '.format(i-j))

nome = len(nomeQuebrado[0])
print(('{} - Quantidade de caracteres do primeiro nome: {}'.format(nomeQuebrado[0], nome)))




