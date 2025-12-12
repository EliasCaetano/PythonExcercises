from random import randint
while True:

    print('=-=' * 9)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-=' * 9)

    try:
        jogar = input('Gostaria de jogar? (S/N): ').upper().strip()
        if jogar not in ['S', 'N']:
            raise ValueError('Insira uma resposta válida (S/N)')
    except ValueError:
        print('Insira uma resposta válida!')
        continue

    if jogar == 'N':
        print('Até a próxima!')
        break

    cont = 0

    while True:
        try:
            n_usuario = int(input('Insira seu número (até 10): '))
            if n_usuario > 10:
                raise ValueError('Insira um número menor que 10!')

            tipo = input('Qual você escolhe? (Par/Impar): ').upper().strip()
            if tipo not in ['PAR', 'IMPAR']:
                raise ValueError('Insira uma opção válida -> (Par/Impar)')

        except ValueError:
            print('Insira um valor válido!')

        n_maquina = randint(1,10)
        soma = n_usuario + n_maquina
        resultado = 'PAR' if soma % 2 == 0 else 'IMPAR'

        if tipo == resultado:
            print('Parabéns, você ganhou!')
            cont += 1
        else:
            print('Você perdeu!')
            print(f'Você venceu {cont} partida(s)')
            break




