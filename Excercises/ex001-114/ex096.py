def area(l, c):
    a = l * c
    print(f'A área do terreno é de {a}m²')

print('MEDIDOR DE TERRENOS'.center(30))
print('-=-' * 10)
a = float(input('Largura: '))
b = float(input('Comprimento: '))
area(a, b)