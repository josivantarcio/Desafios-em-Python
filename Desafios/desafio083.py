expressao = list()
expressao.append(str(input('Digite a expressão: ')))
for i in expressao:
    i.split()
    d = i.count(')')
    e = i.count('(')
if d == e:
    print('Expressão Correta!')
else:
    print('Erro na Expressão')
print(expressao)