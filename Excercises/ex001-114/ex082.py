numeros = []
numeros_pares = []
numeros_impares = []

while True:
    try:
        num = int(input('Insira um número (000 para sair): '))
        if num == 000:
            break
        if num not in numeros:
            numeros.append(num)
    except ValueError:
        print('Valor inserido inválido!')
        continue

pos = 0
while pos < len(numeros):
    if numeros[pos] % 2 == 0:
        numeros_pares.append(numeros[pos])
    else:
        numeros_impares.append(numeros[pos])
    pos += 1

print(f'Valores inseridos -> {numeros}')
print(f'Valores pares -> {numeros_pares}')
print(f'Valores impares -> {numeros_impares}')