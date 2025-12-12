while True:
    try:
        a = int(input('Digite o 1º número: '))
        b = int(input('Digite o 2º número: '))
        c = int(input('Digite o 3º número: '))
        d = int(input('Digite o 4º número: '))
        break
    except ValueError:
        print('Digite um número válido!')
        continue

numeros = (a, b, c, d)
print(f'\nO número 9 apareceu {numeros.count(9)} vez(es)')
if 3 in numeros:
    print(f'O número 3 aparece pela primeira vez na {numeros.index(3) + 1}ª posição')
print(f'Números pares inseridos: ')
for numero in numeros:
    if numero % 2 == 0:
        print(numero)