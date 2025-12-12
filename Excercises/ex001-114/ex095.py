time = []

while True:
    jogador = {}
    jogador['nome'] = input('Nome do jogador: ')

    while True:
        partidas = input(f'Quantas partidas {jogador['nome']} jogou? ')
        if partidas.isdigit():
            jogador['partidas'] = int(partidas)
            break
        print("Entrada inválida. Digite um número.")

    gols = []
    for partida in range(jogador['partidas']):
        gol_partida = int(input(f'Quantos gols {jogador['nome']} fez na partida {partida+1}? '))
        gols.append(gol_partida)

    jogador['gols'] = gols
    jogador['total_gols'] = sum(gols)

    time.append(jogador)

    while True:
        cont = str(input('Quer continuar? (S/N)\n')).upper().strip()
        if cont in ('S', 'N'):
            break
        else:
            print('Insira uma opção válida.')
    if cont == 'N':
        break

print("\n" + "-"*50)
print(f"{'COD':<4}{'NOME':<20}{'GOLS':<18}{'TOTAL':>6}")
print("-"*50)
for i, j in enumerate(time):
    print(f"{i:<4}{j['nome']:<20}{str(j['gols']):<18}{j['total_gols']:>6}")
print("-"*50)

while True:
    escolha = input("Mostrar dados de qual jogador? (digite o COD ou 'S' para sair): ").strip()
    if escolha.upper() == 'S':
        print("Encerrando visualização. Até logo.")
        break
    if not escolha.isdigit():
        print("Digite um código válido ou S para sair.\n")
        continue
    cod = int(escolha)
    if cod < 0 or cod >= len(time):
        print(f"Código inexistente. Digite um número entre 0 e {len(time) - 1}.\n")
        continue

    selecionado = time[cod]
    print("\n" + "-" * 40)
    print(f'Levantamento do jogador {selecionado['nome']}:\n')
    for partida, g in enumerate(selecionado['gols'], start=1):
        print(f'    No jogo {partida} fez {g} gol(s).')
    print(f'\n  Total de gols: {selecionado['total_gols']}.')
    print("\n" + "-" * 40)
