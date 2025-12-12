from Excercises.ex115.lib.interface import *
from Excercises.ex115.lib.arquivo import *
from time import sleep as s

from Excercises.ex115.lib.interface import leiaint

#Main Program
arquivo = 'cadastro.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Pessoas Cadastradas', 'Cadastrar Nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        # Opção para listar o conteúdo do arquivo com o registro de pessoas.
        lerArquivo(arquivo)

    elif resposta == 2:
        # Opção para cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arquivo, nome, idade)

    elif resposta == 3:
        cabecalho('Saindo do sistema... até logo!')
        break

    else:
        print('ERRO! Selecione uma opção válida!')
    s(2)
