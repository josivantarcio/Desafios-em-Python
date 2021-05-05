def aumentar(n=0, p=0, br=False):
    """A atividade da funcao eh pegar o valor digitado pelo usuario no codigo principal e faz o acrescimo no valor com base 
    da variavel solicitada logo após.

    Args:
        n (float, optional): Recebe o valor da variavel para calculo. Defaults to 0.
        p (float, optional): Percentual para calculo. Defaults to 0.
        br (bool, optional): Se falso, valor padrao do sistema, senao converte para brasileiro. Defaults to False.

    Returns:
        float: Retorna o valor calculado para a variavel principal(n)
    """
    v = n + (n * p / 100)
    if br == False:
        return v
    else:
        return moeda(v)


def diminuir(n=0, p=0, br=False):
    """A atividade da funcao eh pegar o valor digitado pelo usuario no codigo principal e faz a reducao no valor com base 
    da variavel solicitada logo após.

    Args:
        n (float, optional): Recebe o valor da variavel para calculo. Defaults to 0.
        p (float, optional): Percentual para calculo. Defaults to 0.
        br (bool, optional): Se falso, valor padrao do sistema, senao converte para brasileiro. Defaults to False.

    Returns:
        float: Retorna o valor calculado para a variavel principal(n)
    """
    v = n - (n * p / 100)
    if br == False:
        return v
    else:
        return moeda(v)


def dobro(n=0, br=False):
    """Vai dobrar o valor fornecido.

    Args:
        n (float, optional): Recebe o valor da variavel para calculo. Defaults to 0.
        br (bool, optional): Se falso, valor padrao do sistema, senao converte para brasileiro. Defaults to False.

    Returns:
        float: Retorna o valor calculado para a variavel principal(n)
    """
    v = n * 2
    if br == False:
        return v
    else:
        return moeda(v)


def metade(n=0, br=False):
    """A funcao vai dividir o valor pela metade.

    Args:
        n (float, optional): Recebe o valor da variavel para calculo. Defaults to 0.
        br (bool, optional): Se falso, valor padrao do sistema, senao converte para brasileiro. Defaults to False.

    Returns:
        float: Retorna o valor calculado para a variavel principal(n)
    """
    v = n / 2
    if br == False:
        return v
    else:
        return moeda(v)


def moeda(n=0,preco='R$'):
    """Funcao recebe o valor principal e converte para o padrao brasileiro (,) e acrescenta mais uma casa decimal.

    Args:
        n (float, optional): Variavel principal recebida para ser tratado no novo formato. Defaults to 0.
        preco (str, optional): Texto de identificacao da moeda convertida. Defaults to 'R$'.

    Returns:
        str: Retorna um texto formatado com R$, mais o valor calculado, substituindo o ponto(.) pela virgula(,).
    """
    return f'{preco}{n:.2f}'.replace('.',',')


def dizimo(n=0, br=False):
    """Calcula a 10ª parte de um valor.

    Args:
        n (float, optional): Valor principal para ser calculado. Defaults to 0.
        br (bool, optional): Se falso, valor padrao do sistema, senao converte para brasileiro. Defaults to False.

    Returns:
        float: Retorna o valor calculado em 10%
    """
    v =  n - (n - (n * 0.1))
    if br == False:
        return v
    else:
        return moeda(v)