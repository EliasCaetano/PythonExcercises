#programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for i in range(10):
    PA = n + i * r
    if i == 9:
        print(PA, end='.')
    else:
        print(PA, end=', ')