from random import choice

q = int(input('quantidade de alunos? '))
nome = []
for i in range(q):
    x = (input('Digite o nome do aluno: '))
    nome.append(x)
sorteado = choice(nome)
print('O aluno sorteado foi... {}'.format(sorteado))
