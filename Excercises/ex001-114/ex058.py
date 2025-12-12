import random
from time import sleep

while True:
    jogar = str(input('Quer jogar um jogo de adivinha? (S/N)\n')).upper().strip()
    while jogar not in ('S', 'N'):
        print('Valor inválido, por favor insira um valor válido: (S/N)')
        jogar = str(input('Quer jogar um jogo de adivinha? (S/N): ')).upper().strip()

    if jogar == 'N':
        print('Que pena, aguardo você numa próxima!')
        break

    print('Legal, vamos jogar!')
    sleep(2)
    print('Vou pensar em um número entre 0 e 10 e você vai tentar adivinha-lo!')
    sleep(2)
    print('Preparado? Vou pensar em um número...')
    sleep(2)
    print('Pronto, já tenho um número!')
    sleep(2)

    numero = random.randint(0, 10)
    tentativas = 0

    while True:
        try:
            resposta = int(input('Qual número você acha que eu escolhi? '))
        except ValueError:
            print('Por favor, digite um valor válido!')
            continue

        tentativas += 1

        if resposta == numero:
            print(f'Parabéns, você acertou! Eu escolhi o número {numero}')
            print(f'Você acertou em {tentativas} tentativa(s)!')
            sleep(1)
            print('Obrigado por jogar!')
            break

        elif resposta != numero:
             print(f'Não foi este número que eu escolhi, tente de novo!')

    restart = input('Quer jogar novamente? (S/N): ').upper().strip()
    while restart not in ('S', 'N'):
        print('Valor inválido, digite S ou N.')
        restart = input('Quer jogar novamente? (S/N): ').upper().strip()

    if restart == 'N':
        print('Quem sabe numa próxima, foi legal jogar com você!')
        break










