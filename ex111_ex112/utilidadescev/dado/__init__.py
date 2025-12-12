def leiaDinheiro(valor):
    valido = False
    while not valido:
        entrada = str(input(valor)).replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'ERRO: \"{valor}\" é um valor inválido.')
        else:
            valido = True
            return float(entrada)
