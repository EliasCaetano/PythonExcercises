total_gasto = 0
produtos_acima_1000 = 0
nome_produto_mais_barato = ''
preco_produto_mais_barato = None
cont = 1

while True:
    print('-' * 26)
    print('LEITURA DE PRODUTOS'.center(26))
    print('-' * 26)
    print(f'PRODUTO {cont}\n')

    nome_produto = input('NOME DO PRODUTO: ')

    while True:
        try:
            preco_produto = float(input('PREÇO: R$ '))
            cont += 1
            total_gasto += preco_produto
            if preco_produto_mais_barato is None or preco_produto < preco_produto_mais_barato:
                    nome_produto_mais_barato = nome_produto
                    preco_produto_mais_barato = preco_produto
            if preco_produto > 1000:
                produtos_acima_1000 += 1
            break
        except ValueError:
            print('DIGITE UM VALOR VÁLIDO!')
            continue

    while True:
        continuar = input('GOSTARIA DE CADASTRAR OUTRO PRODUTO? (S/N): ').strip().upper()
        if continuar in ['S', 'N']:
            break
        print('DIGITE UMA OPÇÃO VÁLIDA!')

    if continuar == 'N':
        print('CADASTRAMENTO ENCERRADO!')
        print(f'TOTAL GASTO: {total_gasto:.2f}')
        print(f'PRODUTOS ACIMA DE R$ 1000: {produtos_acima_1000}')
        print(f'PRODUTO MAIS BARATO: {nome_produto_mais_barato}')
        break


