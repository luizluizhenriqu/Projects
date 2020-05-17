import shelve
from meuSitemaShelve.lib.interface import cabeçalho
from meuSitemaShelve.lib.Pessoas import Pessoa
from random import randint,choice #disponivel somente na versão de dev

def verificarArqExs(nome):
    #dever retornar bool
    try:
        arq = shelve.open(nome, 'r')
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

def verClasses(save):
    #DEV ver classes
    arq = shelve.open(save)
    for dado in arq['lista']:
        print(dado.status())


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
    #mostrar lista
    for key, item in enumerate(arq['lista']):
        print(f'\t\033[33m{key+1:<4}\033[34m{item[0]:<25}{item[1]:>8}\033[m')
    while True:
        #pergunta se quer apagar alguém após aparece a lista
        resp = input('Gostaria de apagar um desses arquivos:? [S/N]').upper()
        if resp in 'sS':
            apagarPessoa(save)
            return None
        else:
            arq.close()
            return None

    #perguntar se quer apagar algum dado do arquivo

def cadastrarPessoa(save, nome, idade=0):
    arq = shelve.open(save)
    lista = arq['lista']
    dado = Pessoa(nome, idade, geraEmailSite(nome))
    #implementação da classe pesso
    #dado = [nome.title(), idade]
    lista.append(dado)
    arq['lista'] = lista

    arq.close()



def geraEmailSite(nome, site=False):
    '''
    Função que gera automaticamente um email ou site
    :param nome:
    :param site: True pra gerar um sitey
    :return:
    '''
    def geraNum(n):
        # def pode ser simplificada e retorna uma string
        while True:
            listnum = [chr(n) for n in range(48, 58)]  # ↓↓↓↓
            num = ''.join([choice(listnum) for i in range(n)])
            # verificar se o primeiro dig de num é 0
            if num[0] == '0':
                continue
            return num
    saida = ('.com.br', '.com', '.org', '.dev')
    provedor = ('g1', 'gmail', 'yahoo', 'outlook',
                'hotmail', 'uol', 'terra', 'globomail',
                'oimail', 'directmail', 'e-mail', 'plugoo')
    person = ('moeda', 'solto', 'planet', 'ferros',
              'mexicana',
              geraNum(randint(2,4)))
    if site:
        site = 'www' + nome.lower().replace + choice(person) +choice(saida)
        return site

    email = nome.lower().replace(' ', '') + choice(person) + '@' + \
            choice(provedor) + \
            choice(saida)
    return email

def cadastrarAuto(save):
    #função teste
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
        #Pergunta qual pessoa apagar
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
        # Pergunta se tem certeza
        try:
            resp=input(f'Você tem certeza que quer apagar {arq["lista"][inde-1][0]}?[S/N]')
            if resp.isdigit() or resp not in 'SsNn': raise ValueError
        except:
            print('Comando inválido, por favo tente novamente: ')
        else:
            if resp in 'Ss':
                #Apagando pessoas da lista
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
