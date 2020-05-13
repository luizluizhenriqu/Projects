import shelve

def verificarArqExs(nome):
    #dever retornar bool
    try:
        arq = shelve.open(nome,'r')
    except:
        return False
    else:
        arq.close()
        return True




def criarArquivo(nome):
    arq = shelve.open(nome, 'c')
    arq['lista'] = []
    arq.close()
    print('\033[34mComo não há data um arquivo criado com sucesso\033[m')


def verPessoas(arq):
    print('okok')
    arq = shelve.open(arq)
    print(f'\033[33m{"Nº":<4}\033[34m{"NOME":<30}{"IDADE":>8}\033[m')
    print('-'*42)
    for key, item in enumerate(arq['lista']):
        print(f'\t\033[33m{key+1:<4}\033[34m{item[0]:<25}{item[1]:>8}\033[m')
    while True:
        try:
            resp = input('Gostaria de apagar um desses arquivos:? [S/N]').upper()
            if resp in 'sS':
                respInde = input('Qual nº:')
                apagarPessoa(respInde)

                print(f'Pessoa apagada') #adicionar nome de pessoa apagada na string
                break
            elif resp in 'nN':
                break
            else: raise ValueError
        except: print('Opção invélidade, tente novamente. ')
    arq.close()

    #perguntar se quer apagar algum dado do arquivo

def cadastrarPessoa(arq, nome, idade=0):
    arq = shelve.open(arq)
    lista = arq['lista']
    dado = [nome.title(), idade]
    lista.append(dado)
    arq['lista'] = lista

    arq.close()




def apagarPessoa(inde):
    pass