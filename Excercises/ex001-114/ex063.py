while True:
    print('Sequência de Fibonnacci')
    print('-=-' * 8)

    try:
        n = int(input('Digite um número inteiro: '))
    except ValueError:
        print('Digite um número válido!\n')
        continue

    seq = int(input('Quantos elementos da sequência deseja ver? '))
    a, b = n, n + 1
    cont = 0

    while cont <= seq:
        if cont == seq:
            print(a, end= ' ... ')
        else:
            print(a, end = ' - ')
        a, b = b, a + b
        cont += 1
    break

