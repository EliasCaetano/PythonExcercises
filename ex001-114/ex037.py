n = int(input('Digite um número: '))
tipo = input('Digite o tipo de base que gostaria de converter (bin/oct/hex): ').lower()

if tipo == 'bin':
    print(f'O número {n} convertido para binário é: {bin(n)}')
elif tipo == 'oct':
    print(f'O número {n} convertido para octal é: {oct(n)}')
elif tipo == 'hex':
    print(f'O número {n} convertido para hexadecimal é: {hex(n)}')
else:
    print('Base inserida inválida')

