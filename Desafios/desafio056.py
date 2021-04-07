idadeMaior = 0
idadeMedia = 0
nomeHomemVelho = ' '
mulheres = 0
for i in range(1, 5):
    nome = str(input('Digite o nome da pessoa n{}: '.format(i))).upper().strip()
    idade = int(input('Digite a idade da pessoa n{}: '.format(i)))
    sexo = str(input('Digite o sexo da pessoa n{}: '.format(i))).upper().strip()
    idadeMedia += idade
    idadeMedia = idadeMedia / i

    if i == 1 and sexo in 'Mm':
        nomeHomemVelho = nome
        idadeMaior = idade
    if sexo in 'Mm' and idadeMaior < idade:
        idadeMaior = idade
        nomeHomemVelho = nome

    if sexo in 'Ff' and idade < 20:
        mulheres += 1

print('A média das idades é de {:.1f} anos'.format(idadeMedia))
print('O Homem mais velho do grupo {} tem {} anos'.format(nomeHomemVelho, idadeMaior))
print('O grupo possui {} Mulher com idade abaixo de 20 anos'.format(mulheres))