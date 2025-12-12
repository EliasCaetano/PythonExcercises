#1 litro de tinta = 2m² de pintura

a = float(input('Digite a altura da parede (m): '))
l = float(input('Digite a largura da parede (m): '))
area = a * l
litro = area / 2

print('A área total a ser pintada é de {}m²\nPara fazer a pintura completa serão necessários {} litros de tinta'.format(area, litro))



