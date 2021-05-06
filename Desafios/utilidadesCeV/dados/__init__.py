def leiaDinheiro(v):
    """A funcao leiaDinheiro(), que vai funcionar de forma semelhante a funcao input() do Python, so que 
    fazendo a validacao para aceitar apenas um valor monetarios. 
    
    Args:
        v (string): get the data in text format and push in the funcion ''leiaDinheiro()'' for to be valided.

    Returns:
        float: after the text be valided for float, the value return to the variable.
    """
    while True:
        num = str(input(v)).replace(',','.').strip()
        if num.isalpha() or num == '':
            print('ERRO! valor invalido')
        else:
            return float(num)
            break
        
        
def leiaInt(msn):
    """A funcao leiaInt(), que vai funcionar de forma semelhante a funcao input() do Python, so que 
    fazendo a validacao para aceitar apenas um valor numerico. 

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