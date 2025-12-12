def leiaint(msg):
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            break
        else:
            print('ERRO, digite um número inteiro válido')
    return numero


#Main Program
n = leiaint('Digite um número inteiro: ')
print(f'Você digitou o número {n}')
