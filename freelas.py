from typing import List
from abc import ABC, abstractmethod
from datetime import datetime

class Pessoa(ABC):
    nome : str
    __cpf : int
    email : str
    telefone : int
    data_nascimento: str

    def __init__(self, nome, cpf, email, telefone, data_nascimento):
        self.nome = nome
        self.__cpf = cpf
        self.email = email
        self.telefone = telefone
        self.data_nascimento = data_nascimento

    def get_cpf(self):
        return self.__cpf

    @abstractmethod
    def informacoes(self):
        pass

    def __str__(self):
        return self.informacoes()
    
class Freelancer(Pessoa):
    atividade_principal : str
    competencias : str
    experiencias : str

    def __init__(self, nome, cpf, email, telefone, data_nascimento, atividade, competencias, experiencias):
        super().__init__(nome, cpf, email, telefone, data_nascimento)
        self.atividade_principal = atividade
        self.competencias = competencias
        self.experiencias = experiencias

    def idade(self):
        nascimento = datetime.strptime(self.data_nascimento, "%d/%m/%Y")
        hoje = datetime.today()
        return hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

    def informacoes(self):
        return (f'Nome: {self.nome}\n'
                f'Idade: {self.idade()}\n'
                f'Email: {self.email}\n'
                f'Telefone: {self.telefone}'
                f'\nAtividade: {self.atividade_principal}\n'
                f'Competências: {self.competencias}\n'
                f'Experiências: {self.experiencias}\n')
    
class Contratante(Pessoa):
    __cnpj: int
    empresa: str

    def __init__(self, nome, cpf, email, telefone, data_nascimento, cnpj, empresa):
        super().__init__(nome, cpf, email, telefone, data_nascimento)
        self.__cnpj = cnpj
        self.empresa = empresa

    def get_cnpj(self):
        return self.__cnpj

    def informacoes(self):
        return (f'Nome: {self.nome}\n'
                f'Telefone: {self.telefone}\n'
                f'Email: {self.email}\n'
                f'CNPJ: {self.__cnpj}\n'
                f'Empresa: {self.empresa}\n')
    
class Projeto:
    id_projeto: int
    empresa : str
    titulo : str
    data : str
    hora : str
    atividades : str
    valor : float
    contratante : Contratante
    freelancers : List[Freelancer]

    def __init__(self, id_projeto, empresa, titulo, data, hora, atividades, valor, contratante):
        self.id_projeto = id_projeto
        self.empresa = empresa
        self.titulo = titulo
        self.data = data
        self.hora = hora
        self.atividades = atividades
        self.valor = valor
        self.contratante = contratante
        self.freelancers = []

    def __str__(self):
        return (f'Titulo: {self.titulo}\n'
                f'Empresa: {self.empresa}\n'
                f'Data: {self.data}\n'
                f'Hora: {self.hora}\n'
                f'Atividades: {self.atividades}\n'
                f'Valor: {self.valor}\n')

    def add_freelancer(self, freelancer):
        self.freelancers.append(freelancer)

class Gerenciamento:
    def __init__(self):
        self.projetos: List[Projeto] = []
        self.freelancers: List[Freelancer] = []

    def add_freelancer(self, novo_freelancer: Freelancer):
        for f in self.freelancers:
            if f.get_cpf() == novo_freelancer.get_cpf():
                raise Exception("Freelancer já cadastrado com este CPF!")

        self.freelancers.append(novo_freelancer)

    def listar_freelancers(self):
        print("\nDescrição de cada Freelancer:\n")
        if not self.freelancers:
            print("Nenhum freelancer cadastrado.\n")
        else:
            for f in self.freelancers:
                print(f)

    def add_projeto(self, novo_projeto: Projeto):
        for p in self.projetos:
            if p.id_projeto == novo_projeto.id_projeto:
                raise Exception("Projeto já cadastrado!")
        
        self.projetos.append(novo_projeto)

    def listar_projetos(self):
        print("\nDescrição de cada Projeto:\n")
        if not self.projetos:
            print("Nenhum projeto cadastrado")
        else: 
            for p in self.projetos:
                print(p)
