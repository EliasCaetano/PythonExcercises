from time import sleep

def maior(num):
    if max(num) != 0:
        print('-'*30)
        print(f'Foram informados {len(num)} valores:'.center(30))
        for c in num:
            print(f'\n> {c}')
            sleep(0.5)
        print('-'*30)
        print(f'O maior número informado foi {max(num)}')
    else:
        print('-'*30)
        print(f'Foram informados {len(num)} valores:'.center(30))
        for c in num:
            print(f'\n> {c}')
            sleep(0.5)
        print('-' * 30)
        print(f'O maior número informado foi {max(num)}')


#Main Program
numeros = [-10, -7, -5, 0]
maior(numeros)
numeros = [10, -5, 3, 0, 23, 13, 16]
maior(numeros)