from random import randint

a = randint(1,100)
b = randint(1,100)
c = randint(1,100)
d = randint(1,100)
e = randint(1,100)

numeros = (a, b, c, d, e)
print(f'Números sorteados: {numeros}')
print(f'Maior número sorteado: {max(numeros)}')
print(f'Menor número sorteado: {min(numeros)}')
