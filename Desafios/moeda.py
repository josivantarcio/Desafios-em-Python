def aumentar(n=0, p=0):
    return n + (n * p / 100)


def diminuir(n=0, p=0):
    return n - (n * p / 100)


def dobro(n=0):
    return n * 2


def metade(n=0):
    return n / 2


def moeda(n=0,preco='R$'):
    return f'{preco}{n:.2f}'.replace('.',',')


def dizimo(n=0):
    return n - (n - (n * 0.1))