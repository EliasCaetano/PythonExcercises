from datetime import datetime

ano_nasc = int(input('Qual seu ano de nascimento? '))
idade = datetime.now().year - ano_nasc

if idade > 18:
    print('O período de alistamento já passou!')
    print(f'Você está atrasado em {idade - 18} anos')
elif idade == 18:
    print('Você está na idade exata para se alistar!')
else:
    print(f'Ainda falta(m) {18 - idade} ano(s) para você se alistar!')
