a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('As retas podem formar um triângulo!')
    if a == b == c:
        print('Será formado um triângulo EQUILÁTERO (todos os lados iguais).')
    elif a == b or a == c or b == c:
        print("O triângulo é ISÓSCELES (dois lados iguais).")
    else:
        print("O triângulo é ESCALENO (todos os lados diferentes).")
else:
    print('As retas não podem formar um triângulo.')