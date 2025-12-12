cadastro = []

while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: ')).strip().title()

    while True:
        sexo = input("Sexo [M/F]: ").strip().upper()
        if sexo in ('M', 'F'):
            pessoa['sexo'] = sexo
            break
        print("Entrada inválida. Digite M para masculino ou F para feminino.")

    while True:
        idade_str = input("Idade: ").strip()
        if idade_str.isdigit():
            pessoa['idade'] = int(idade_str)
            break
        print("Entrada inválida. Digite um número inteiro para a idade.")

    cadastro.append(pessoa)

    while True:
        resp = input("Deseja cadastrar outra pessoa? [S/N]: ").strip().upper()
        if resp in ('S', 'N'):
            break
        print("Resposta inválida. Digite S para sim ou N para não.")
    if resp == 'N':
        break

total = len(cadastro)
print("\n" + "-" * 40)
print(f"A) Total de pessoas cadastradas: {total}")

if total > 0:
    soma_idades = sum(p['idade'] for p in cadastro)
    media = soma_idades / total
    print(f"B) Média de idade: {media:.2f}")
else:
    media = 0
    print("B) Média de idade: 0.00")

mulheres = [p['nome'] for p in cadastro if p['sexo'] == 'F']
print("C) Mulheres cadastradas:", mulheres if mulheres else "Nenhuma")

acima_media = [p for p in cadastro if p['idade'] > media]
if acima_media:
    print("D) Pessoas com idade acima da média:")
    for p in acima_media:
        print(f" - {p['nome']}, {p['idade']} anos, sexo {p['sexo']}")
else:
    print("D) Pessoas com idade acima da média: Nenhuma")
print("-" * 40)