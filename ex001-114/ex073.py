times = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Bahia', 'Fluminense', 'Atlético-MG',
         'Botafogo', 'Mirassol', 'Corinthians', 'Grêmio', 'Ceará SC', 'Vasco da Gama', 'São Paulo', 'Santos',
         'EC Vitória', 'Internacional', 'Fortaleza', 'Juventude', 'Sport Recife')

print('Os primeiros 5 colocados são:')
for time in range(0,5):
    print(f'{time + 1}º - {times[time]}')

print('\nOs 4 últimos colocados são:')

for pos, time in enumerate(times[-4:], start=17):
    print(f'{pos}º - {time}')

print('\nTimes em ordem alfabética:')
for time in sorted(times):
    print(time)

print('\nPosição atual do time do Grêmio:')
print(f'O Grêmio está atualmente na {times.index('Grêmio')}ª posição.')