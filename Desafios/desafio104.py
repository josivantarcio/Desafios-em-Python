def leiaInt(msn):
    """A funcao leiaInt(), que vai funcionar de forma semelhante a funcao input() do Python, so que 
    fazendo a validacao para aceitar apenas um valor numerico. 
    Ex: n = leiaInt('Digite um n: ')

    Args:
        msn (string): get the data in text format and push in the funcion ''leiaInt()'' for to be valided.

    Returns:
        integer: after the text be valided for integer, the value return to the variable and right after is print.
    """
    while True:
        valor = str(input(msn))
        if msn.isnumeric():
            valor = int(msn)
        if valor.isnumeric():
            break
        else:
            print('ERRO! Você não digitou um número.')
    return valor


n = leiaInt('Digite um número: ')
print(f'O valor digitado foi: {n}')
