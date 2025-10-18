# módulo main_funcionario.py


from classes_filhas_funcionario import *
from classe_funcionario import *
from exececoes_funcionario import *

# OBSERVAÇÃO: AS EXECEÇÕES SERAM TESTADAS  COM ERROS, PARA QUE ASSIM VEJAMOS SE AS PRINCIPAIS EXECEÇÕES ESTÃO FUNICONANDO.


try:
    teste1=Professor(1,'abc4567',1600,'Mestre')
except NomeInvalidoError as e:
    print(f'{e}')
except SalarioNegativoError as r:
    print(f'{r}')
except Exception as r:
    print(f'{r}')




try:
    teste2=TecnicoAdministrativo('Lara Kelly','1234567',-5000,'Auxiliar de RH')
except NomeInvalidoError as e:
    print(f'{e}')
except SalarioNegativoError as r:
    print(f'{r}')
except Exception as r:
    print(f'{r}')



try:
    teste2=Terceirizado('Maria','1234568',1200,'Tytersyt',True)
except NomeInvalidoError as e:
    print(f'{e}')
except SalarioNegativoError as r:
    print(f'{r}')
except Exception as r:
    print(f'Erro: {r}')


# TESTE VERDADEIROS
print('-'*20)
teste3=Terceirizado('Julia','1234567',2000,'Valid',True)
print(teste3.aumentar_salario(10))

print(teste3.detalhar_funcionario())
