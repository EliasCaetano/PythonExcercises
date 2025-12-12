matriz = [
    [],
    [],
    []
]

print('MATRIZ 3X3'.center(30))
print('-=-' * 10)

for i in range(9):
    matriz_valor = int(input(f'Insira o {i+1}º valor: '))
    if len(matriz[0]) < 3:
        matriz[0].append(matriz_valor)
    elif len(matriz[1]) < 3:
        matriz[1].append(matriz_valor)
    else:
        matriz[2].append(matriz_valor)

print('MATRIZ 3X3 - RESULTADO')
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')

