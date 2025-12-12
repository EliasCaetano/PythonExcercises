print('=' * 35)
print('BANCO CAETANO - SIMULAÇÃO DE SAQUE'.center(35))
print('=' * 35)

while True:
    try:
        valor = int(input('DIGITE O VALOR QUE DESEJA SACAR (R$): '))
        if valor <1:
            print('Valor inválido, tente novamente.')
            continue
        break
    except ValueError:
        print('Por favor, insira um número inteiro válido!')

cedulas = [50, 20, 10, 1]
resultado = {}

for cedula in cedulas:
    quantidade = valor // cedula
    valor %= cedula
    if quantidade > 0:
        resultado[cedula] = quantidade

print('\nCÉDULAS ENTREGUES:')
for cedula, quantidade in resultado.items():
    print(f'{quantidade} cédula(s) de R$ {cedula}')