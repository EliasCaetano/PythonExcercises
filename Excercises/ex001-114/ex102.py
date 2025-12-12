from time import sleep

def fatorial(n=1, show:str = ''):
    f = 1
    if show == 'SIM':
        for i in range(1, n+1):
            f *= i
            print(f'{f}', end=' ')
            sleep(0.5)
    else:
        for i in range(1, n+1):
            f *= i
        print(f'{f}', end=' ')


#Main Program
n = int(input('Número a fatorar: '))
show = input('Deseja ver o cálculo passo a passo? (SIM/NAO): ').upper().strip()
fatorial(n, show)






