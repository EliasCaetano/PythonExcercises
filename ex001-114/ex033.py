numeros = []

print('Digite a seguir 3 números e descubra qual o maior e o menor número digitado')
for i in range(3):
    item = float(input(f"Digite o {i +1}º número: "))
    numeros.append(item)
print(f'Os números inseridos foram: {numeros}')
maior = max(numeros)
menor = min(numeros)
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
