soma_idade = 0
homem_mais_velho = {'nome': '', 'idade': 0}
mulheres_menos_20 = 0

for i in range(1,5):
    print(f'\nPessoa {i}:')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip().upper()
    soma_idade += idade
    if sexo == 'M' and idade > homem_mais_velho['idade']:
        homem_mais_velho['nome'] = nome
        homem_mais_velho['idade'] = idade
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media_idade = soma_idade / 4

print("\nResultados:")
print(f"A média de idade do grupo é {media_idade:.2f} anos.")
if homem_mais_velho["nome"]:
    print(f"O homem mais velho é {homem_mais_velho['nome']}, com {homem_mais_velho['idade']} anos.")
else:
    print("Não há homens no grupo.")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")