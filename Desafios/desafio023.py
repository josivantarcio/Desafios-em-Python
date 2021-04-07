milhar = int(input('Digite uma milhar: '))
u = milhar // 1 % 10
d = milhar // 10 % 10
c = milhar // 100 % 10
m = milhar // 1000 % 10
print('\033[1;33munidade: {:}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))