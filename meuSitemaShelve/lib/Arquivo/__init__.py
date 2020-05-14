import shelve
from meuSitemaShelve.lib.interface import cabeçalho
from random import randint

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


def verPessoas(save):
    print(' okok')
    arq = shelve.open(save)
    if len(arq['lista']) == 0:
        #verificar se tem algum dado salvo na data base
        print(' Nenhum dado salvo. ')
        arq.close()
        return False
    print(f'\033[33m{"Nº":<4}\033[34m{"NOME":<30}{"IDADE":>8}\033[m')
    print('-'*42)
    for key, item in enumerate(arq['lista']):
        print(f'\t\033[33m{key+1:<4}\033[34m{item[0]:<25}{item[1]:>8}\033[m')
    while True:

        resp = input('Gostaria de apagar um desses arquivos:? [S/N]').upper()
        if resp in 'sS':
            apagarPessoa(save)
        else:
            return None

        print('Opção invélidade, tente novamente. ')
        #print(e)
    arq.close()

    #perguntar se quer apagar algum dado do arquivo

def cadastrarPessoa(save, nome, idade=0):
    arq = shelve.open(save)
    lista = arq['lista']
    dado = [nome.title(), idade]
    lista.append(dado)
    arq['lista'] = lista

    arq.close()

def cadastrarAuto(save):
    arq = shelve.open(save)
    randNome = ['lisandra', 'michael', 'marcos', 'ze carlos', 'washigton', 'vilma', 'daniele',
                'michele', 'palyne', 'amanda', 'rayane', 'poliane', 'bruna', 'elaine', 'felipe']
    lista = arq['lista']
    for nome in randNome:
        dado = [nome.title(), randint(1, 99)]
        lista.append(dado)
    arq['lista'] = lista
    arq.close()
    print('prontooooooooooooooooooooo')





def apagarPessoa(save, inde=0):
    print('Apagando...')
    arq = shelve.open(save)
    while True:
        if inde == 0:
            try:
                inde = int(input('Digite o número de cadastro da pessoa: '))
                if inde == 0:
                    raise ValueError
            except:
                print('Comando inválido, por favo tente novamente')
            else: break
        else:
            print('pulou primeiro laço')
            break
    while True:
        try:
            resp=input(f'Você tem certeza que quer apagar {arq["lista"][inde-1][0]}?[S/N]')
            if resp.isdigit() or resp not in 'SsNn': raise ValueError
        except:
            print('Comando inválido, por favo tente novamente: ')
        else:
            if resp in 'Ss':
                lista = arq['lista']
                print(f'apagando {lista[inde-1]}')
                lista.pop(inde-1)
                arq['lista'] = lista

                break
            else:
                print('Comando cancelado. ')
                break
    arq.close()
    return None



    for item in arq['lista']:
        print(item)