def linha(tam=29):
    return f'=' * tam

def leiaInt(n=0):
    while True:
        try:
            valor = int(input(n))
            break
        except (ValueError, TypeError):
            print('\033[31mErro. Digite valor valido\033[m')
    return valor

def cabecalho(msg):
    print(linha())
    print(msg.center(29).upper())
    print(linha())
    
def menu(lista):
    cabecalho('menu principal')
    for k, v in enumerate(lista):
        print(f'{k+1}: {v}')
    print(linha())
    opcao = leiaInt('Sua Opção: ')
    return opcao
    
def final():
    print(linha())
    print('ATÉ LOGO | SEE YOU LATER!'.center(29))
    print(linha())