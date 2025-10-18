# módulo classe_funcionario.py

from abc import ABC,abstractmethod
from exececoes_funcionario import *

# classe abstrata(base para as demais classes)
class FuncionarioUniversitario(ABC):
    def __init__(self,nome,matricula:str,salario_base):
        self.nome=nome
        self.matricula=matricula
        self.salario_base=salario_base


    # métodos property e setter para acessa e modificar os atributos privados
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,novo_nome):
        if  not isinstance(novo_nome,str) or not novo_nome.strip():
            raise NomeInvalidoError('Erro, você deve preenche o campo e informar um nome do tipo string.')
        self.__nome=novo_nome

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self,nova_matricula):
        if not isinstance(nova_matricula,str) or len(nova_matricula) !=7:
            raise MatriculaInvalidaError('Erro, a matricula deve contém exatamente 7 caracteres.')
        self.__matricula=nova_matricula


    @property
    def salario_base(self):
        return self.__salario_base
    
    @salario_base.setter
    def salario_base(self,novo_salario):
        if novo_salario<=0:
            raise SalarioNegativoError('Erro, não permintimos sálario negativo.')
        self.__salario_base=novo_salario

# métodos abstratos
   
    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def detalhar_funcionario(self):
        pass


    # método concreto
    def aumentar_salario(self,percentual):
        return self.salario_base+percentual



