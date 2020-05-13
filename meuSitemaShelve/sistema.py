from meuSitemaShelve.lib.interface import *
from meuSitemaShelve.lib.Arquivo import *
from time import sleep

def main():
    arq = 'savesnomes.db'
    if not verificarArqExs(arq):
        criarArquivo(arq)
    while True:
        resp = menu('DATABASE',['Ver Pessoas', 'Cadastra Pessoa', 'Apagar Pessoa', 'Sair', 'Testar arq'])
        if resp == 1:
            #Ver Pessoas
            verPessoas(arq)
        elif resp == 2:
            #Cadastra Pessoa
            nome = input('Nome: ')
            idade = leiaInt('Idade: ')
            cadastrarPessoa(arq, nome, idade)
        elif resp == 3:
            #Apagar Pessoa
            pass
        elif resp == 4:
            #Sair
            break
        elif resp == 5:
            pass
        else: print('\033[31mPor favor digite um número valido: \033[m')
        sleep(0.9)



if __name__ == '__main__':
    #arq = 'savesnomes.db'
    #verPessoas(arq)
    main()

