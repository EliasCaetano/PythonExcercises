from datetime import datetime

maioridade = 0
menoridade = 0

for i in range(7):
    year = int(input('Insira seu ano de nascimento: '))
    if year > datetime.now().year:
        print('Ano inserido é inválido')
        continue
    current_age = datetime.now().year - year
    if current_age < 18:
        menoridade += 1
    else:
        maioridade += 1
print(f'O número de maiores de idade é: {maioridade}')
print(f'O número de menores de idade é: {menoridade}')