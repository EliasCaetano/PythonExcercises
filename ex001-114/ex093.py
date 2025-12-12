jogador = {}

jogador['nome'] = input('Nome do jogador: ')
jogador['partidas'] = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

gols = []
for partida in range(jogador['partidas']):
    gol_partida = int(input(f'Quantos gols {jogador['nome']} fez na partida {partida+1}? '))
    gols.append(gol_partida)

jogador['gols'] = gols
jogador['total_gols'] = sum(gols)

print('-=' * 25)
print(jogador)
print('-=' * 25)

for campo, valor in jogador.items():
    print(f'O campo {campo} tem o valor {valor}')
print('-=' * 25)

print(f'O jogador {jogador['nome']} fez {jogador['partidas']} partidas:')
for i in range(jogador['partidas']):
    print(f'--> Na partida {i+1}, fez {gols[i]}')
print(f'Total de {jogador['total_gols']} gol(s) em {jogador['partidas']} partida(s)')