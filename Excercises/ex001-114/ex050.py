n = []

for i in range(1,7):
    nx = int(input(f'Digite o {i}º número: '))
    if nx % 2 == 0:
        n.append(nx)

soma = sum(n)

print(n)
print(f'A soma dos números pares inseridos é: {soma}')
