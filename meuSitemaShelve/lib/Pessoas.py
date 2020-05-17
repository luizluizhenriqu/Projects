class Pessoa:
    def __init__(self, Nome, Idade, Email):
        '''
        Construtor da classe conta
        :param Nome:
        :param Idade:
        :param Email:
        '''
        self.nome = Nome
        self.idade = Idade
        self.email = Email

    def __str__(self):
        '''
        quando a classe é printada
        devolve uma string representando a conta

        :return:
        '''
        return f'Nome: {self.nome} \nIdade: {self.idade} \nEmail: {self.email}'

    def status(self):
        return (self.nome, self.idade, self.email)
