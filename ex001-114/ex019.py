import random

alunos = [''] * 4
alunos[0] = input('Digite o nome do primeiro aluno: ')
alunos[1] = input('Digite o nome do segundo aluno: ')
alunos[2] = input('Digite o nome do terceiro aluno: ')
alunos[3] = input('Digite o nome do quarto aluno: ')
rand = random.choice(alunos)

print("O aluno escolhido para apagar o quadro é: {}".format(rand))
