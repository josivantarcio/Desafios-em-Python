cidade = input('Digite o nome da sua cidade: ')
cidade = cidade.lower()
cidadeq = cidade.split()
if cidadeq[0] == 'santo':
    print('A cidade {}, começa nome de Santo! '.format(cidade))
else:
    print('A cidade {}, não inicia com nome de santo {}!'.format(cidade, cidadeq[0]))