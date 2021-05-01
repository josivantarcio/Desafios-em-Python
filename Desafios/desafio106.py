def ajuda(msn):
    """Funcao de apresentar o help em Python

    Args:
        msn (str): Faz chamada para a variavel fun do programa principal

    Returns:
        str: Retorno da funcao help do Python
    """
    print('\033[0;34;47m')
    return help(msn)

def corCabecalho():
    """Imprime o cabecalho colorido
    """
    print('\033[0;33;45m')
    print('=' * 19)
    print('  AJUDA DO SISTEMA')
    print('=' * 19)

def corRodape():
    """Imprime o rodapé colorido
    """
    print('\033[0;30;46m')
    print('=' * 19)
    print('   FIM')
    print('=' * 19)
    
    
#main
while True:
    corCabecalho()
    fun = str(input('Digite a ajuda: ')).strip()
    if fun in 'fim':
        break
    else:
        desc = ajuda(fun)
corRodape()