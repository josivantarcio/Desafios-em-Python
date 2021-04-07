pessoa = {}
grupo = []
muheres = []
acimaMedia = []
soma = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo M/F: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! Favor digitar apenas M ou F!')
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    while True:
        stp = str(input('Deseja continuar? (S/N) ')).strip()[0].lower()
        if stp in 'sn':
            break
        else:
            print('ERRO! Favor entrar com S ou N!')
    if stp in 'n':
        break
print('='* 40)
#A
print(f'Total de Pessoas {len(grupo)}')
#B
for i in grupo:
    soma += i['idade']
media = soma / len(grupo)
print(f'Media de Idade é de {media:.2f} anos')
#C
print('=' * 40)
print('       == Lista de Mulheres ==')
for i in grupo:
    if i['sexo'] == 'F':
        muheres.append(i)
for i in muheres:
    print(f" -> {i['nome']:<7} com idade de {i['idade']} anos")
print(f"Total de ========== {len(muheres)}")
#D
print('=' * 40)
print('     == Lista Acima da Média ==')
for i in grupo:
    if i['idade'] > media:
        acimaMedia.append(i)
for i in acimaMedia:
    print(f" -> {i['nome']:<7} com idade de {i['idade']} anos do sexo: {i['sexo']}")
print(f"Total de ========== {len(acimaMedia)}")