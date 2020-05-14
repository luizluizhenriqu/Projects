def cabeçalho(txt='', tam=42):

    def linha(extInicio='',extFim=''):
        print(extInicio, '-'*tam, extFim)
    linha('\033[36m','\033[m')
    print('\033[33m',txt.center(tam).upper(),'\033[m')
    linha('\033[36m','\033[m')

def leiaInt(msg='Digite um número inteiro: '):
    while True:# batata
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número inteiro valido.\033[m')
            continue
        except KeyboardInterrupt: #esta bosta não funciona aqui
            print('\033[31mEntrada de dados interrompida pelo usúario\033[m')
            return 0
        else:
            return n

def menu(titulo, lista):
    cabeçalho(titulo)
    while True:
        for cont, op in enumerate(lista):
            print(f'\t\033[33m{cont+1} - \033[34m{op}\033[m')
        cabeçalho()

        return leiaInt('\033[35m Sua opção: \033[m')


