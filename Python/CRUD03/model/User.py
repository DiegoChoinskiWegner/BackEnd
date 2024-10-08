class User():
    def __init__(self, nome, idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade
    
    def set_idade(self, idade):
        self.__idade = idade

    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email