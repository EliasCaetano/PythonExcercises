nome_cidade = input('Digite o nome da cidade: ').strip()
primeira_palavra = nome_cidade.split()[0].upper()
if primeira_palavra == "SANTO":
    print('O nome da cidade começa com SANTO')
else:
    print("O nome da cidade não começa com SANTO")

