from time import sleep

def contador(i, f, p):
    if p == 0:
        p = 1
    elif p < 0:
        p *= -1

    if i < f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
    else:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p


i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)