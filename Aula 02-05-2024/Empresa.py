'''
ATIVIDADE PRÁTICA 3

Crie uma classe Empresa que permita gerenciar
funcionários. Os funcionários devem ter informações
como nome, cargo e salário. A empresa deve ser capaz

de adicionar, remover e listar funcionários.
'''
class Funcionario:
    def __init__(self, nome: str, cargo: str, salario: float) -> None:
        self.nome = nome
        self.cargo = cargo
        self.salario = salario


class Empresa:
    def __init__(self) -> None:
        self.funcionarios = []
        
    def adicionar(self, funcionario:Funcionario):
        self.funcionarios.append(funcionario)
    
    def listar(self):
        if len(self.funcionarios) == 0:
            print('Não existe funcionario cadastrado')
        else:
            for funcionario in self.funcionarios:
                print(funcionario.nome)
                print(funcionario.cargo)
                print(funcionario.salario)
                
    def remover(self, nome: str):
        i = 0
        for funcionario in self.funcionarios:            
            if nome == funcionario.nome:
                # print('Teste')
                # print(i)
                # print(self.funcionarios[0].nome)
                               
                del(self.funcionarios[i])
                
                # print(type(self.funcionarios))
            i += 1            

fun1 = Funcionario('Leonardo', 'Programador', 19.800)
fun2 = Funcionario('Jose', 'Designer', 19.800)

emp = Empresa()

emp.adicionar(fun1)
emp.adicionar(fun2)
emp.listar()
emp.remover('Leonardo')
emp.listar()
            
        
        