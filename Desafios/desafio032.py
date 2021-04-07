from datetime import date
ano = int(input('Digite o ano desejado: '))
if ano == 0:
    ano = date.today().year
if(ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0):
    print('{} é Bissexto'.format(ano))
else:
    print('{} não é Bissexto'.format(ano))
