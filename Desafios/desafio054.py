from datetime import date
today = date.today().year
maior = 0
menor = 0
for i in range(1,8):
    idade = int(input('Digite o ano de nascimento: '))
    if (today - idade) >= 18:
        maior += 1
    else:
        menor += 1
print('Maiores: {}\nMenores: {}'.format(maior, menor))