expressao = str(input('Digite a expressão: '))
parenteses = []

for caracter in expressao:
    if caracter == '(':
        parenteses.append('(')
    elif caracter == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break

if len(parenteses) == 0:
    print('Expressão Correta!')
else:
    print('Expressão Incorreta!')