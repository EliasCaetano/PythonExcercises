from http.cookiejar import uppercase_escaped_char

tipo = input('Informe o tipo de temperatura (C, F, K): ').upper()
temp = float(input('Digite a temperatura: '))

if tipo == 'C':
    k = temp + 273
    f = temp * 1.8 + 32
    print('Temperatura em K: {:.2f}\nTemperatura em F: {:.2f}'.format(k,f))
elif tipo == 'F':
    k = (temp-32) * 5/9 + 273
    c = (temp-32) / 1.8
    print('Temperatura em K: {:.2f}\nTemperatura em C: {:.2f}'.format(k,c))
elif tipo == 'K':
    f = (temp-273) * 1.8 + 32
    c = temp - 273
    print('Temperatura em F: {:.2f}\nTemperatura em C: {:.2f}'.format(f,c))
else:
    print('Informação inserida da maneira errada')

