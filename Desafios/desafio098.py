def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i <= f:
        for x in range(i, f+p, p):
            print(x, end=" ", flush=True)
            sleep(0.5)
        print('Fim')
    if f <= i:
        for x in range(i, f-p, -p):
            print(x, end=" ", flush=True)
            sleep(0.5)
        print('Fim')


from time import sleep
#main
contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
print('FIM')