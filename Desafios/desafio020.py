from random import shuffle
n = int(input('Quantidade de Alunos: '))
nome = []
for x in range(n):
    n = (input('Digite o nome do Aluno nº {}: '.format(x+1)))
    nome.append(n)
shuffle(nome)
print(nome)


