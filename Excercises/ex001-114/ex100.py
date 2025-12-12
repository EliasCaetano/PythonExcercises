from random import randint

numeros = []

def sorteia():
    for i in range(0, 5):
        numeros.append(randint(0, 20))
    print(f'Números Sorteados: {numeros}')
def soma_par():
    s = 0
    print('Números pares:', end=' ')
    for i in range(len(numeros)):
        if numeros[i] % 2 == 0:
            print(numeros[i], end=' ')
            s += numeros[i]
    print(f'\nSoma dos pares: {s}')


#Main Program
sorteia()
soma_par()




