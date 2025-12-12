numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    try:
        n = int(input('Insira um número entre 0 e 20: '))
        if n < 0 or n > 20:
            raise ValueError('Digite um valor válido.')
        break
    except ValueError:
        print('Digite uma opção válida!')
        continue

print(f'O número {n} por extenso é {numeros[n]}')
