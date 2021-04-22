def layout(texto, i):
    print('=' * (i))
    print(f'  {texto}')
    print('=' * (i))


#main
txt = str(input('Digite um texto: ')).upper()
cont = len(txt) + 4
layout(txt, cont)