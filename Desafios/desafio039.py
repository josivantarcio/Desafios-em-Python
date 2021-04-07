from datetime import date
ano = int(input('informe o ano de nascimento '))
anoSys = date.today().year
idade = anoSys-ano
print(idade)
if idade < 18:
    tempo = 18 - idade
    print('\033[1;33mAinda vai se alistar!, falta {} anos'.format(tempo))
elif idade == 18 or idade == 19:
    print('\033[1;33mHora de se Alistar!')
elif idade > 19:
    tempo = idade - 19
    print('\033[1;33mPassou do Tempo! Já se passaram {} anos'.format(tempo))
print('Seu ano foi/será em {}'.format(ano+18))