from random import randint
cpu = randint(0,5)
usuario = int(input('Digite um numero entre 0 a 5: '))
if(cpu == usuario):
    print('\033[33;mAcertô, mizeravi!')
else:
    print('Errou Zé Ruela')