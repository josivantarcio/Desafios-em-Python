from random import randint
n = int(input('Digite um numero: '))
cpu = randint(0, 10)
cont = 0
while n != cpu:
    cont += 1
    print('Errou! Tentar novamente...')
    n = int(input('Digite um numero: '))
    print('*' * 20)
print('Acertou!')
print('Foram {} tentativas'.format(cont))