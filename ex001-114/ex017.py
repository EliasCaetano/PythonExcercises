cat_op = float(input('Digite o valor do cateto oposto: '))
cat_ad = float(input('Digite o valor do cateto adjacente: '))
hip = (cat_op ** 2) + (cat_ad ** 2)

print('O valor da hipotenusa, considerando cateto oposto = {} e cateto adjascente = {}, é de = {}'.format(cat_op,cat_ad,hip ** 1/2))
