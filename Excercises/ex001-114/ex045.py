import random
from time import sleep

print('\033[1;35m----------------------\033[m')
print('\033[1;35m       JOKENPÔ\033[m')
print('\033[1;35m----------------------\033[m')
print('\033[1;34mGostaria de jogar?\033[m')
print('(1) Sim\n(2) Não')

jogar = input('Selecione uma opção: ').strip().upper()
opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
item_aleatorio = random.choice(opcoes)

if jogar == '1' or jogar == 'SIM' :
    print('Certo, vamos jogar!')
    print('Vou contar até 3. No 3, escolha pedra, papel ou tesoura.')
    sleep(1)
    for i in range(1, 4):
        print(i)
        sleep(1)
    usuario = input('Faça sua escolha: ').strip().upper()
    print(f'Eu escolho \033[1;34m{item_aleatorio}\033[m')
    if item_aleatorio == 'PEDRA':
        if usuario == 'PEDRA':
            print('EMPATE!')
        elif usuario == 'PAPEL':
            print('VOCÊ VENCEU!')
        elif usuario == 'TESOURA':
            print('VOCÊ PERDEU!')
        else:
            print('\033[1;31mJOGADA INVÁLIDA!\033[m')

    if item_aleatorio == 'PAPEL':
        if usuario == 'PEDRA':
            print('VOCÊ PERDEU!')
        elif usuario == 'PAPEL':
            print('EMPATE!')
        elif usuario == 'TESOURA':
            print('VOCÊ VENCEU!')
        else:
            print('\033[1;31mJOGADA INVÁLIDA!\033[m')

    if item_aleatorio == 'TESOURA':
        if usuario == 'PEDRA':
            print('VOCÊ VENCEU!')
        elif usuario == 'PAPEL':
            print('VOCÊ PERDEU!')
        elif usuario == 'TESOURA':
            print('EMPATE!')
        else:
            print('\033[1;31mJOGADA INVÁLIDA!\033[m')
elif jogar == '2' or jogar == 'NÃO' or jogar == 'NAO':
    print('Que pena, aguardo você na próxima!')
else:
    print('OPÇÃO INVÁLIDA!')