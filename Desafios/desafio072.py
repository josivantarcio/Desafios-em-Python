ext = ('zero', 'um', 'dois', 'tres','quatro','cinco',
       'seis','sete','oito','nove','dez',
       'onze','doze','treze','quatorze','quinze',
       'dezesseis','sezessete','dezoito','dezenove','vinte')
while True:
    while True:
        n = int(input('Digite um número: '))
        if n >= 0 and n <= 20:
            break
    print(ext[n])
    rt = str(input('Quer continnuar? S/N ')).strip().upper()[0]
    if rt in 'Nn':
        break
print('FIM')