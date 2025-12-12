pesos = []

for i in range(1,6):
    kg = float(input(f'Digite o {i}º peso: '))
    pesos.append(kg)

maior_peso = max(pesos)
menor_peso = min(pesos)

print(f'Pesos inseridos: {pesos}')
print(f'O maior peso é: {maior_peso:.2f}')
print(f'O menor peso é: {menor_peso:.2f}')