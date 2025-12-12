n1 = int(input('Digite um número: '))

for i in range(1,11,1):
    if n1 != 0:
        n2 = n1 * i
        print('{} x {} = {}'.format(n1,i,n2))
else:
    print('Impossível fazer a tabuada do 0')
