print('Soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500')
soma = 0
cont = 0
for i in range(1,501,2):
    if i % 3 == 0:
        soma += i
        cont += 1
print(f'A soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500 é: {soma}')
print(f'Total de números múltiplos de 3 no intervalo: {cont}')
