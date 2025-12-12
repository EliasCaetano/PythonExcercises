while True:
    n = int(input('Digite o primeiro termo da PA: '))
    r = int(input('Digite a razão da PA: '))
    cont = 0

    while cont < 10:
        PA = n + cont * r
        cont += 1
        if cont == 10:
            print(f'{PA}', end='.')
        else:
            print(f'{PA} ', end='> ')
    break
