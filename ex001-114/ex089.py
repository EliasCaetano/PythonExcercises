alunos = []

print('-=' * 20)
print('REGISTRO DE NOTAS'.center(40))
print('-=' * 20)

while True:
    try:
        nome = str(input('ALUNO(A): '))
        print('-' * 25)
        nota_1 = float(input('1ª NOTA: '))
        nota_2 = float(input('2ª NOTA: '))
        media = (nota_1 + nota_2) / 2
        print('-' * 25)
        alunos.append([nome,[nota_1, nota_2], media])

        while True:
            continuar = str(input('Gostaria de continuar? (S/N): ')).lower().strip()
            print('-' * 25)
            if continuar not in ('s', 'n'):
                print('OPÇÃO INVÁLIDA!')
            elif continuar in ('s', 'n'):
                break
        if continuar == 'n':
            break

    except ValueError:
        print('INFORMAÇÃO INVÁLIDA!')
        continue

print('MÉDIAS FINAIS'.center(25))
print('-' * 25)

for sublista in alunos:
    print(f'ALUNO(A) - {sublista[0]}\nMÉDIA FINAL - {sublista[2]}')
    print('-' * 15)

while True:
    consultar = str(input('Gostaria de consultar as notas de algum aluno? (S/N): ')).lower().strip()

    print('-' * 25)
    if consultar not in ('s', 'n'):
        print('OPÇÃO INVÁLIDA!')
    elif consultar in 'n':
        break

    print('> LISTA DE ALUNOS <')
    for indice, aluno in enumerate(alunos):
        print(f'{indice + 1} - {aluno[0]}')
    print('-' * 25)

    escolha_nota = int(input('QUAL ALUNOS DESEJA CONSULTAR (Nº)? '))
    print('-' * 25)
    if 1 <= escolha_nota <= len(alunos):
        nome, notas, media = alunos[escolha_nota - 1]
        print(f'NOTAS DO ALUNO(A) - {nome}\n1ª NOTA: {notas[0]}\n2ª NOTA: {notas[1]}')
        print('-' * 25)

if consultar == 'n':
    print('PROGRAMA ENCERRADO')
    exit()


