def layout(texto, i):
    print('=' * (i+3))
    print(f' {texto}')
    print('=' * (i+3))


txt = str(input('Digite um texto: ')).upper()
cont = len(txt)
layout(txt, cont)
