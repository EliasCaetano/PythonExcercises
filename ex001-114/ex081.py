numeros = []

while True:
    try:
        num = int(input('Insira um número (000 para sair): '))
        if num == 000:
            break
        else:
            numeros.append(num)
    except ValueError:
        print('Valor inserido inválido!')
        continue

print(f'Número de valores inseridos -> {len(numeros)}')
print(f'Lista de valores decrescente -> {sorted(numeros, reverse=True)}')
print(f'O número 5 está na lista?',end=' ')

if 5 in numeros:
    print('SIM')
else:
    print('NÃO')