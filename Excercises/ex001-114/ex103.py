def ficha(nome = '', gols=0):
    print('-=-' * 11)
    print('FICHA DE JOGADOR'.center(33))
    print('-=-' * 11)
    print(f'O jogador {nome} fez {gols} gols')


#Main Program
nome = str(input('Digite o nome do jogador: '))
try:
    gols = int(input(f'Quantos gols {nome} fez? '))
except ValueError:
    gols = 0
ficha(nome, gols)