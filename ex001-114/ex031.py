dist = float(input('Qual a distância da viagem em KMs? '))
if dist <= 200:
    custo_viagem = dist * 0.5
    print(f'O valor total da sua viagem é de: R$ {custo_viagem}')
elif dist > 200:
    custo_viagem = dist * 0.45
    print(f'O valor total da sua viagem é: R$ {custo_viagem}')
else:
    print('O valor inserido não é valido')

