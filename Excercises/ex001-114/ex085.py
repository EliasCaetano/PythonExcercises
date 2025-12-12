numeros = [[],[]]

for n in range(7):
    num = int(input(f'Digite o {n + 1}º número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()

print(numeros)
print(f'Pares -> {numeros[0]}')
print(f'Impares -> {numeros[1]}')