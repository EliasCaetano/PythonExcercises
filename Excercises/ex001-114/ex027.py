nome = str(input('Insira seu nome completo: ')).upper().strip()
n = nome.split()
print('Seu nome completo é: {}'.format(nome))
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu último nome é : {}'.format(n[len(n)-1]))

