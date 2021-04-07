saque = int(input('Informe o valor desejado para saque! R$ '))

if saque >= 100:
    conte100 = saque // 100
    saque = saque % 100
    if conte100 != 0:
        print(f'{conte100} cédula(s) de 100,00')

if saque >= 50:
    conte50 = saque // 50
    saque = saque % 50
    if conte50 != 0:
        print(f'{conte50} cédula(s) de 50,00')

if saque >= 20:
    conte20 = saque // 20
    saque = saque % 20
    if conte20 != 0:
        print(f'{conte20} cédula(s) de 20,00')

if saque >= 10:
    conte10 = saque // 10
    saque = saque % 10
    if conte10 != 0:
        print(f'{conte10} cédula(s) de 10,00')

if saque >= 5:
    conte5 = saque // 5
    saque = saque % 5
    if conte5 != 0:
        print(f'{conte5} cédula(s) de 5,00')

if saque >= 1:
    conte1 = saque // 1
    saque = saque % 1
    if conte1 != 0:
        print(f'{conte1} cédula(s) de 1')
