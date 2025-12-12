numeros = []
for num in range(0,5):
    try:
        numeros.append(int(input('Insira um número: ')))
    except ValueError:
        print('Valor inserido inválido!')

print(f'Valores inseridos -> {numeros}')
print(f'Maior número inserido: {max(numeros)} na {numeros.index(max(numeros)) + 1}ª posição')
print(f'Menor número inserido: {min(numeros)} na {numeros.index(min(numeros)) +1}ª posição')

