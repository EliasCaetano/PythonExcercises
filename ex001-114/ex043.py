altura = float(input('Digite sua altura (em metros): '))
peso = float(input('Digite seu peso (kg): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é: {imc:.2f}')
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é: {imc:.2f}')
    print('Você está no peso ideal')
elif 25 <= imc < 30:
    print(f'Seu IMC é: {imc:.2f}')
    print('Você está com sobrepeso')
elif 30 <= imc < 40:
    print(f'Seu IMC é: {imc:.2f}')
    print('Você está com obesidade')
else:
    print(f'Seu IMC é: {imc}')
    print('Você está com obesidade mórbida')