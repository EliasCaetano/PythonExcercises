from datetime import datetime

trabalhador = {}

trabalhador['nome'] = input('Nome: ')
trabalhador['ano_nascimento'] = int(input('Ano de Nascimento: '))
trabalhador['idade'] = datetime.now().year - trabalhador['ano_nascimento']
trabalhador['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['CTPS'] != 0:
    trabalhador['ano_contratacao'] = int(input('Ano de Contratação: '))
    trabalhador['salario'] = float(input('Salário: R$ '))
    trabalhador['aposentadoria'] = 35 - (datetime.now().year - trabalhador['ano_contratacao'])

print('-=' * 25)
for k, v in trabalhador.items():
    print(f'- {k}: {v}')