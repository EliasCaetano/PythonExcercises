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

print('-=-' * 10)
print('MATRIZ 3X3 - RESULTADO')
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
print('-=-' * 10)

pares = []
for sublista in matriz:
    for num in sublista:
        if num % 2 == 0:
            pares.append(num)
print(f'Soma dos números pares -> {sum(pares)}')

terceira_coluna = [coluna[2] for coluna in matriz]
print(f'Soma dos valores da terceira coluna -> {sum(terceira_coluna)}')
print(f'Maior valor da segunda linha -> {max(matriz[1])}')


