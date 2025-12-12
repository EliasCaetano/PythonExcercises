maior_18 = 0
homens = 0
mulheres_U20 = 0
cont = 1

while True:
    print('=-' * 13)
    print('CADASTRO DE PESSOA FÍSICA')
    print('=-' * 13)
    print(f'Nº DE CADASTRO: {cont}')

    while True:
        try:
            idade = int(input('IDADE: '))
            if idade > 18:
                maior_18 += 1
            break
        except ValueError:
            print('DIGITE UM NÚMERO VÁLIDO!')
            continue

    while True:
        try:
            sexo = input('SEXO (M/F): ').upper().strip()
            if sexo not in ['M', 'F']:
                raise ValueError('DIGITE UMA OPÇÃO VÁLIDA!')
            elif sexo == 'M':
                homens += 1
            elif sexo == 'F' and idade < 20:
                mulheres_U20 += 1
            break
        except ValueError:
            print('DIGITE UMA OPÇÃO VÁLIDA!')
            continue

    cont += 1

    try:
        continuar = input('GOSTARIA DE CADASTRAR MAIS UMA PESSOA? (S/N) -> ').upper().strip()
        if continuar not in ['S', 'N']:
            raise ValueError('DIGITE UMA OPÇÃO VÁLIDA!')
        elif continuar == 'N':
            print('CADASTRAMENTO FINALIZADO')
            print('DADOS CADASTRADOS:')
            print(f'Pessoas com mais de 18 anos: {maior_18}')
            print(f'Homens cadastrados: {homens}')
            print(f'Mulheres com menos de 20 anos: {mulheres_U20}')
            break
    except ValueError:
        print('DIGITE UMA OPÇÃO VÁLIDA!')




