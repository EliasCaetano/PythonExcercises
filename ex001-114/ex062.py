while True:
    n = int(input('Digite o primeiro termo da PA: '))
    r = int(input('Digite a razão da PA: '))
    cont = 0
    adicionar_termos = 10
    total = 0

    while adicionar_termos != 0:
        total = total + adicionar_termos
        while cont < total:
            PA = n + cont * r
            cont += 1
            if cont == total:
                print(f'{PA}', end=' > ...')
            else:
                print(f'{PA} ', end='> ')

        adicionar_termos = int(input('\nQuantos termos você quer mostrar a mais? '))
    break
print('PROGRAMA ENCERRADO!')

