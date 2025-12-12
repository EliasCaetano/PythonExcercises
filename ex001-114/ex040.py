n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 7:
    print('Parabéns, você está \033[1;4;32mAPROVADO\033[m')
    print(f'Sua média final é {m:.2}')
elif m > 5 < 7:
    print('Você precisará fazer uma recuperação.')
    print(f'Sua média final é {m:.2}')
else:
    print('Você está \033[1;4;31mREPROVADO\033[m')
    print(f'Sua média final é {m:.2}')
