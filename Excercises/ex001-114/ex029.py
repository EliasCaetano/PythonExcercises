from random import randint
from time import sleep

print('-' * 31)
print('Programa de Radar de Velocidade')
print('-' * 31)
print('Medindo velocidade...')
velocidade = randint(60,120)
sleep(3)
print(f'Velocidade medida pelo radar: {velocidade}Km/h')
print('Limite de velocidade da via: 80Km/h')
if velocidade > 80:
    print('Velocidade acima da permitida na via, você será multado!')
    multa = (velocidade - 80) * 7
    print(f'Valor total da multa: R$ {multa}')
elif velocidade <= 80:
    print('Velocidade dentro do limite permitido na via')
