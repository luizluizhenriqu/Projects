from meuSitemaShelve.lib.interface import *
from meuSitemaShelve.lib.Arquivo import *
from time import sleep

def main():
    arq = 'savesnomes.db'
    if not verificarArqExs(arq):
        criarArquivo(arq)
    while True:
        resp = menu('DATABASE',['Ver Pessoas', 'Cadastra Pessoa', 'Apagar Pessoa',
                                'Sair', 'Testar arq', 'teste cadastrar', 'Ver classes cadastradas'])
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
            apagarPessoa(arq,0)
        elif resp == 4:
            #Sair
            break
        elif resp == 5:
            # teste apagado
            pass
        elif resp == 6:
            #teste DEV auto adicionar contatos
            cadastrarAuto(arq)
        elif resp == 7:
            # teste DEV pra Ver classes salvas

            verClasses(arq)
        else: print('\033[31mPor favor digite um número valido: \033[m')
        sleep(0.9)



if __name__ == '__main__':
    #arq = 'savesnomes.db'
    #verPessoas(arq)
    main()

