salario = float(input('Digite o seu salário atual: R$ '))
if salario > 1250.00:
    novo_salario = salario * 1.10
    print(f'Seu novo salário com o aumento será de: R$ {novo_salario:.2f}')
else:
    novo_salario = salario * 1.15
    print(f'Seu novo salário com o aumento é de: R$ {novo_salario:.2f}')