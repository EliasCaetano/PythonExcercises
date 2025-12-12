n = int(input('Digite um número: '))
for i in range(1,11,1):
    if n != 0:
        n2 = n * i
        print('{} x {} = {}'.format(n,i,n2))
    else:
        print('Impossível fazer a tabuada do 0')
        exit()