cont = 0
soma = 0

while True:
    try:
        n = int(input('Digite um número (999 para sair): '))
    except ValueError:
        print('Digite um número válido!')
        continue

    if n == 999:
        break
    cont += 1
    soma += n
    
print(f'A soma dos {cont} números inseridos é {soma}.')


