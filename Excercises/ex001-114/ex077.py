palavras = (
    'Lâmpada',
    'Horizonte',
    'Gelado',
    'Maravilha',
    'Travesseiro',
    'Labirinto',
    'Caneta',
    'Eclipse',
    'Borboleta',
    'Relâmpago'
)

print('-' * 30)
print('VOGAIS NAS PALAVRAS'.center(30))
print('-' * 30)

for palavra in palavras:
    vogais = []
    for letra in palavra.lower():
        if letra in 'aeiouáéíóúâêîôûãõà':
            vogais.append(letra)
    vogais_str = ', '.join(vogais)
    print(f'{palavra:<13} -> {vogais_str}')

