from math import sin, radians, cos, tan
ang = float(input('Digite o valor: '))
sen = sin(radians(ang))
cose = cos(radians(ang))
tang = tan(radians(ang))
print('No angulo de {}, O Seno é {:.2f}, Cosseno é {:.2f} e a Targente é {:.2f}'.format(ang, sen, cose, tang,))