print("Caetano's Car Rental")

km = float(input('Informe a kilometragem rodada: '))
dia = int(input('Informe a quantidade de dias que o carro: '))

print('O valor total do aluguel durante {} dias com {}km rodados é de: R$ {:.2f}'.format(dia,km,(dia * 60) + (km * 0.15)))
