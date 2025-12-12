from random import randint
from time import sleep

dados = {
    f'Jogador {i+1}': randint(1, 6)
    for i in range(4)
}

print('>>> Valores Sorteados <<<')
for k, v in dados.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.65)

ranking = dict(sorted(dados.items(), key=lambda item: item[1], reverse=True))
print('-=' * 15)
print('>>> RANKING DOS JOGADORES <<<')
for posicao, (jogador, valor) in enumerate(ranking.items(), start=1):
    sleep(0.65)
    print(f'{posicao}º lugar — {jogador} com {valor}')