numeros = []

while True:
    try:
        num = int(input('Insira um número (000 para sair): '))
        if num == 000:
            break
        if num not in numeros:
            numeros.append(num)

    except ValueError:
        print('Valor inserido inválido!')

print(f'Números únicos digitados -> {sorted(numeros)}')