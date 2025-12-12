sexo = str(input('Digite o seu sexo (M/F): ')).upper().strip()

while sexo not in ('M', 'F', 'MASCULINO', 'FEMININO'):
    sexo = str(input('Digite um sexo válido (M/F): ')).upper().strip()

print(f'Sexo registrado: {sexo}')


