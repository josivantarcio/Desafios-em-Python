from datetime import date

ano = int(input('Digite o ano de nascimento: '))
anoCorrente = date.today().year
idade = anoCorrente - ano

if(idade <= 9):
    print('Atleta \033[1;34mMirim')
elif(idade <= 14):
    print('Atleta \033[1;34mInfantil')
elif(idade <= 19):
    print('Atleta \033[1;34mJunior')
elif(idade <= 25):
    print('Atleta \033[1;34mSênior')
else:
    print('Atleta \033[1;34mMaster')