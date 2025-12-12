numeros = []

for i in range(0,5):
    try:
        num = int(input('Insira um número: '))
        if i == 0 or num > numeros[-1]:
            numeros.append(num)
        else:
            pos = 0
            while pos < len(numeros):
                if num <= numeros[pos]:
                    numeros.insert(pos, num)
                    break
                pos += 1
    except ValueError:
        print('Valor inserido inválido!')


print(f'Lista ordenada dos números inseridos -> {numeros}')