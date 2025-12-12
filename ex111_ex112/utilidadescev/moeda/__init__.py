def aumentar(n=0.0, taxa_aum=0, format=False):
    taxa = taxa_aum / 100
    if taxa != 0:
        soma = n + (n * taxa)
    else:
        soma = n
    return soma if not format else moeda(soma)

def diminuir(n=0.0, taxa_dec=0, format=False):
    taxa = taxa_dec / 100
    if taxa != 0:
        soma = n - (n * taxa)
    else:
        soma = n
    return soma if not format else moeda(soma)

def dobro(n=0.0,format=False):
    soma = 2*n
    return soma if not format else moeda(soma)

def metade(n=0.0,format=False):
    soma = n/2
    return soma if not format else moeda(soma)

def moeda(n=0.0, moeda='R$'):
    return (f'{moeda}{n:8.2f}'.replace('.', ','))


def resumo(n=0, taxa_aum=0, taxa_dec=0):
    print(f'-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print(f'-' * 30)
    print(f'Preço analisado:{moeda(n):.>19}')
    print(f'Dobro do preço:{dobro(n, True):.>20}')
    print(f'Metade do preço:{metade(n, True):.>19}')
    print(f'{taxa_aum:.2f}% de aumento:{aumentar(n, taxa_aum, True):.>17}')
    print(f'{taxa_dec:.2f}% de desconto:{diminuir(n, taxa_dec,True):.>16}')