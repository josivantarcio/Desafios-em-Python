def ajuda(msn):
    print('\033[1;34;43m')
    return help(msn)

def corCabecalho():
    print('\033[0;33;45m')
    print('=' * 19)
    print('AJUDA DO SISTEMA')
    print('=' * 19)


#main
corCabecalho()
fun = str(input('Digite o codigo: ')).lower().strip()

desc = ajuda(fun)