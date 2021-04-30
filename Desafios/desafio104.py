def leiaInt(msn):
    """Exercício Python 104: Crie um programa que tenha a função leiaInt(), 
    que vai funcionar de forma semelhante ‘a função input() do Python, só que 
    fazendo a validação para aceitar apenas um valor numérico. 
    Ex: n = leiaInt(‘Digite um n: ‘)

    Args:
        msn (string): recebe o dado em formato texto e leva para dentro da função para ser tratada.

    Returns:
        integer: Após o tratamento(validação) do texto para inteiro, o valor retorna para a variavel e logo após é impresso na tela.
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