def leiaint(msg):
    try:
        numero = int(input(msg))
    except (ValueError, TypeError):
        print('ERRO, digite um número inteiro valido!')
        return leiaint(msg)
    else:
        return numero

def leiaFloat(msg):
    try:
        numero = float(input(msg))
    except (ValueError, TypeError):
        print('ERRO, digite um número real valido!')
        return leiaFloat(msg)
    else:
        return numero

#Main Program
n = leiaint('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n} e o número real {n2}')