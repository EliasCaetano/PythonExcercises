from datetime import datetime

ano_nasc = int(input('Digite o seu ano de nascimento: '))
idade = datetime.now().year - ano_nasc
print(f'Idade: {idade} anos')
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade > 9 and idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade > 14 and idade <= 19:
    print('Sua categoria é JÚNIOR')
elif idade > 19 and idade <= 25:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
