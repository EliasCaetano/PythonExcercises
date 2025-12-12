def ajuda(x):
    x = comando.lower()
    help(x)


#Main Program
comando = ''
while comando != 'fim'.lower():
    print('\033[31m-\033[m'*30)
    print("\033[1;33mPyHelp\033[m".center(40))
    print('\033[31m-\033[m'*30)
    comando = input("\033[1;4;33mDigite um comando para obter ajuda\033[m\n-> ")
    if comando == 'fim':
        break
    ajuda(comando)
    print('\033[4;36m(digite "fim" para sair)\033[m')