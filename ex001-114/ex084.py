pessoas = []

print('CADASTRO DE PESSOAS'.center(30))
print('-=-' * 10)

while True:
    try:
        nome = str(input('NOME: '))
        peso = float(input('PESO: '))
        print('-=-' * 10)
        pessoas.append([nome, peso])
        while True:
            continuar = str(input('Gostaria de continuar? (S/N): ')).lower().strip()
            print('-=-' * 10)
            if continuar in ('s', 'n'):
                break
            else:
                print('Opção Inválida!')
                continue
        if continuar == 'n':
            print('>>> CADASTRAMENTO ENCERRADO! <<<')
            print('-=-' * 10)
            break
    except ValueError:
        print('Valor Inválido!')
        continue

print(f'Pessoas Cadastradas - {len(pessoas)}')
mais_pesada = max(pessoas, key=lambda x: x[1])
mais_leve = min(pessoas, key=lambda x: x[1])

print(f'Mais pesada: {mais_pesada[0]} com {mais_pesada[1]}kg')
print(f'Mais leve: {mais_leve[0]} com {mais_leve[1]}kg')





