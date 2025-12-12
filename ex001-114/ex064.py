print('PROGRAMA PARA SOMAR VÁRIOS NÚMEROS')
print('Para sair do programa, digite 999')

soma = 0
cont = 0

while True:
    try:
        n = int(input('Digite um número: '))
    except ValueError:
        print('Por favor, digite um número válido!')
        continue

    if n == 999:
        break

    soma += n
    cont += 1

print(f'O valor somado dos {cont} números é {soma}')

