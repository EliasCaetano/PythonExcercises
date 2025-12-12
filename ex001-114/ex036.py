valor_casa = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual seu salário? R$ '))
pgto_duracao = int(input('Em quantos anos deseja pagar? '))
prestacao_mensal = valor_casa / (pgto_duracao * 12)

if prestacao_mensal > salario * 0.3:
    print('Infelizmente não é possível realizar a solicitação de empréstimo.')
else:
    print('Parabéns, seu emprestimo foi \033[1;4;36mAPROVADO\033[m')
    print(f'Valor total: R$ {valor_casa}')
    print(f'Total de parcelas: {pgto_duracao * 12}')
    print(f'Valor da parcela: R$ {prestacao_mensal:.2f}')
