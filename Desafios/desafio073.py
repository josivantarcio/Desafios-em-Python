times = ('Flamengo','Internacional','Atlético-MG','São Paulo','Fluminense','Grêmio','Palmeiras','Santos',
         'Athletico-PR','Bragantino','Ceará','Corinthians','Atlético-GO',\
        'Bahia','Sport','Fortaleza','Vasco','Goiás','Coritiba','Botafogo')

print(f'Times do Brasileirão 2020/2021: {times}')

print(f'Os cinco primeiros: {times[0:5]}')

print(f'Os quatros últimos: {times[-4:]}')

print(sorted(times))

print(times.index('Flamengo')+1)
