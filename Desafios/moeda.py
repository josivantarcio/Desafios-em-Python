def aumentar(n, p=0):
    return f'O valor de {n} com acrescimo de {p}% é: {n + (n * p / 100)}'


def diminuir(n, p=0):
    return f'O valor de {n} com desconto de {p}% é: {n - (n * p / 100)}'


def dobro(n):
    return f'O dobro de {n} é: {n * 2}'


def metade(n):
    return f'O metade de {n} é: {n / 2}'