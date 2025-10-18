# módulo classes_filhas_funcionario.py


from classe_funcionario import *


class Professor(FuncionarioUniversitario):
    def __init__(self,nome,matricula,salario_base,nivel): #nivel deve ser "mestre" ou "doutor"
      super().__init__(nome,matricula,salario_base)
      self.nivel=nivel

    #   métodos para acessa e modificar atributo: "nivel"
    @property
    def nivel(self):
       return self.__nivel
    
    @nivel.setter
    def nivel(self,novo_nivel):
       tipo_nivel=['Mestre','Doutor']
       if  novo_nivel not in tipo_nivel:
          raise NivelInvalidoError('Erro, o campo nível deve ser preenchido com "Mestre" ou "Doutor". ')
       self.__nivel=novo_nivel


    def calcular_salario(self):
       if self.nivel=='Mestre':
        return self.salario_base *0.15
       elif self.nivel=='Doutor':
          return self.salario_base*0.30

    def detalhar_funcionario(self):
       return f'''Nome: {self.nome}, matricula: {self.matricula}, sálario: {self.salario_base}, 
               seu correspondente nivel: {self.nivel}.'''
    
    def aumentar_salario(self, percentual):
       if percentual<=0:
          raise ValueError ("Informe uma pocertagem válida.")
       aumento=self.salario_base* (1+ percentual)
       return aumento
    


class TecnicoAdministrativo(FuncionarioUniversitario):
   def __init__(self, nome,matricula,salario_base,cargo):
      super().__init__(nome,matricula,salario_base)
      self.cargo=cargo

   # método para acessa e modificar "cargo"
   @property
   def cargo(self):
      return self.__cargo
   
   @cargo.setter
   def cargo(self,novo_cargo):
      if not isinstance(novo_cargo,str) or not novo_cargo.strip():
       raise ValueError ('Erro, você deve informar um cargo do tipo string.')
      self.__cargo=novo_cargo


   def calcular_salario(self):
      salario_adicional=self.salario_base+500
      return salario_adicional
   
   def detalhar_funcionario(self):
      return f'''Nome: {self.nome}, matricula: {self.matricula}, sálario: {self.salario_base}, cargo: {self.cargo}.'''
   
   def aumentar_salario(self, percentual):
      aumento=self.salario_base * percentual + self.salario_base #o calculo consiste em mostrar o valor atualizado com o aumento %
      return aumento
   

class Terceirizado(FuncionarioUniversitario) :
   def __init__(self,nome,matricula,salario_base,empresa,periculosidade): # caso a periculosidade seja "TRUE" á adicional de 10%
      super().__init__(nome,matricula,salario_base)
      if self.salario_base<1500:
         raise SalarioAbaixoError('Erro, um(a) terceirizado deve receber acima de 1500.')
      self.empresa=empresa
      self.periculosidade=periculosidade

   # método para acessar e modifica atributos: "empresa", "periculosidade"
   @property
   def empresa(self):
      return self.__empresa
   
   @empresa.setter
   def empresa(self,nova_empresa):
      if not isinstance(nova_empresa,str):
         raise ImpresaIncorretaError('Erro, você deve preenche o campo com string.')
      self.__empresa=nova_empresa


   @property
   def periculosidade(self):
      return self.__periculosidade
   
   @periculosidade.setter
   def periculosidade(self,nova):
      if not isinstance(nova,bool):
         raise ValueError('Erro, o campo deve ser booleano.')
      self.__periculosidade=nova



   def calcular_salario(self):
      if self.periculosidade==True:
         adicional=self.salario_base* 0.10 + self.salario_base
         return adicional
      return self.salario_base
   

   def detalhar_funcionario(self):
      return f'''Nome: {self.nome}, matricula: {self.matricula}, salario: {self.salario_base},
        empresa de atuação: {self.empresa}, pericuosidade: {self.periculosidade}.'''
   
   def aumentar_salario(self, percentual):
      aumento=self.salario_base*percentual + self.salario_base
      return aumento
      


        