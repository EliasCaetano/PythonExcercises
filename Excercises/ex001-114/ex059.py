while True:
    try:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    except ValueError:
        print('Insira um número válido!')
        continue

    while True:
        print('Escolha a operação desejada: ')
        print('(1) Somar\n(2) Multiplicar\n(3) Maior\n(4) Novos Números\n(5) Sair do programa')
        op = int(input('--> '))

        if op == 1:
            print(f'Soma total: {n1 + n2}')
            break
        elif op == 2:
            print(f'Produto dos números: {n1 * n2}')
            break
        elif op == 3:
            if n1 > n2:
                print(f'O número {n1} é o maior')
            else:
                print(f'O número {n2} é o maior')
            break
        elif op == 4:
            print('Escolha os novos números a seguir...')
            break
        elif op == 5:
            print('PROGRAMA ENCERRADO!')
            quit()
        else:
            print('Digite uma opção válida!')

    if op != 4:
        try:
            restart = input('Gostaria de realizar outra operação? (S/N): ').upper().strip()
        except ValueError:
            print('Insira uma opção válida!')
            continue
        if restart  == 'S':
            continue
        else:
            print('PROGRAMA ENCERRADO!')
            break