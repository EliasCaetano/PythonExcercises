# Criar um programa que faça o computador pensar em um número de 1 a 5 e pedir para o usuário tentar adivinhar qual é esse número
import random
from time import sleep

a = input('Quer jogar um jogo de adivinha? (S/N): ').upper().strip()
if a == 'S':
    print('Certo, vou pensar em um número entre 0 e 5 e você vai tentar adivinha-lo!')
    sleep(1)
    print('Deixa eu pensar...')
    sleep(3)
    print('Pronto, pensei em um número!')
elif a == 'N':
    print('Poxa, que pena! Talvez em uma próxima oportunidade...')
    exit()
else:
    print('Desculpe, não entendi sua resposta...')
    exit()
n = random.randint(0,5)
n_usuario = int(input('Qual número você acha que eu escolhi? '))
if n_usuario == n:
    print('Você acertou, o número que eu pensei é {}, parabéns!'.format(n))
else:
    print('Não foi dessa vez... o número que eu pensei é {}, mais sorte na próxima!'.format(n))

