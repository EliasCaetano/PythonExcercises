valor = float(input('Indique o valor do produto: R$ '))
print('Nossas formas de pagamento são:\n(1) À vista em dinheiro/cheque: 10% de desconto\n(2) À vista no cartão: 5% de desconto\n'
      '(3) Em até 2x no cartão: preço formal\n(4) 3x ou mais no cartão: 20% de juros')
forma_pgto = int(input('Indique a forma de pagamento: '))

if forma_pgto == 1:
    print('Forma de pagamento escolhida: À vista em dinheiro/cheque')
    print(f'O valor final do produto é: R$ {valor * 0.9:.2f}')
elif forma_pgto == 2:
    print('Forma de pagamento escolhida: À vista no cartão: 5% de desconto')
    print(f'O valor final do produto é: R$ {valor * 0.95:.2f}')
elif forma_pgto == 3:
    print('Forma de pagamento escolhida: Em até 2x no cartão: preço formal')
    print(f'O valor final do produto é: R$ {valor:.2f}')
    print(f'Valor da parcela: 2x de R$ {valor / 2:.2f}')
elif forma_pgto == 4:
    print('Forma de pagamento escolhida: 3x ou mais no cartão: 20% de juros')
    print(f'O valor final do produto é: R$ {valor * 1.20}')
    parcela = int(input('Em quantas parcelas gostaria de realizar o pagamento (máx. 36x)? '))
    if 3 <= parcela < 36:
        print(f'Valor da parcela: {parcela}x de R$ {(valor * 1.20) / parcela:.2f}')
    else:
        print('Número de parcelas inserido é inválido!')
else:
    print('Opção de pagamento inválida')
