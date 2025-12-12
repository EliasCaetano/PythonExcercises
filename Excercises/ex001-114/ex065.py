print('PROGRAMA PARA DESCOBRIR MAIOR E MENOR VALOR')

n = []

while True:
    try:
        n.append(int(input('Digite um número: ')))
    except ValueError:
        print('Digite um número válido!')
        continue
    continuar = input('Gostaria de adicionar mais um número? (S/N): ').upper().strip()

    while continuar not in ('S', 'N'):
        print('Por favor, insira uma resposta válida!')
        continuar = input('Gostaria de adicionar mais um número? (S/N): ').upper().strip()
    else:
        if continuar == 'N':
            print(f'O valor mais alto inserido é {max(n)} e o menor valor é {min(n)}.\nA média dos valores inseridos é {sum(n) / len(n)}')
            break

