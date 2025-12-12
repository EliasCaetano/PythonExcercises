import random
from time import sleep

jogos = []
cont = 0

while True:
    try:
        print('-=' * 15)
        cont = int(input('Quantos jogos deseja fazer? '))
        print('-=' * 15)
        break
    except ValueError:
        print('Valor inserido inválido, tente novamente!')
        continue

for jogo in range(cont):
    numeros = []
    while len(numeros) < 6:
        numero = random.randint(1,60)
        if numero not in numeros:
            numeros.append(numero)
    jogos.append(numeros)

for i, jogo in enumerate(jogos, start=1):
    sleep(0.65)
    print(f'Jogo {i} - {sorted(jogo)}')

