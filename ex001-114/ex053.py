phrase = input('Digite uma palavra ou frase para saber se é um palíndromo: ').strip().upper()
words = phrase.split()
jn_words = ''.join(words)
reverse = jn_words[::-1]
if jn_words == reverse:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo')
print(jn_words)
print(reverse)