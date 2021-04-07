n = int(input('Digite um numero: '))
cont = 0
for i in range(1, n+1):
    if n % i == 0:
        print('\033[1;34m',end=' ')
        cont +=1
    else:
        print('\033[m',end=' ')
    print(i,end=' ')
if cont == 2:
    print('\n\033[mPrimo')
else:
    print('\n\033[mNão é Primo')