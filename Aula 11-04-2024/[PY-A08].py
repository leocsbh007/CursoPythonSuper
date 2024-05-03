'''
[PY-A07] Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a chave deste dicionário é o número de matrícula dos próprios alunos. 
O programa deve permitir:
1 - Adicionar
2 - Remover
3 - Atualizar
4 - Listar os alunos.
Para isso, você deve implementar um módulo que contém as seguintes funções:
AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos.
RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos.
AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário .
VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um.
Lembre Se de Modularizar o código
'''
def AdicionarAluno(nome:str, matricula:int):
    # Verifica se este aluno já esta cadastrado
    for a in alunos:
        for v in a.values():
            if v == matricula:
                print("Já existe matricula cadastrada")
                del alunos[v-1]
                break
    
    aluno["Matricula"] = matricula
    aluno["Nome"] = nome
    alunos.append(aluno.copy())

def RemoverAluno(matricula:int):
    # Variavel de controle para verificar se existe aluno na base de dados
    flag_aluno = True
    if len(alunos) == 0:
        print("Não existe nenhum aluno cadastrado")        
    else:
        for a in alunos:
            for v in a.values():
                if v == matricula:
                    del alunos[v-1]
                    # "Suja a flag" para não informar que já tem aluno na base de dados
                    flag_aluno = False
                    break
    # Verifica de a flag esta "Suja"
    if flag_aluno:
        print("Não existe este aluno na Base de Dados")
    

def AtualizarAluno(matricula:int, nome:str):
    # Variavel de controle para verificar se existe aluno na base de dados
    flag_aluno = True
    if len(alunos) == 0:
        print("Não existe nenhum aluno cadastrado")   
    
    else:
        for a in alunos:
            for v in a.values():
                if v == matricula:
                    alunos[v-1]['Nome'] = nome
                    # "Suja a flag" para não informar que já tem aluno na base de dados
                    flag_aluno = False
                    break
    # Verifica de a flag esta "Suja"
    if flag_aluno:
        print("Não existe este aluno na Base de Dados")

def VerAlunos(alunos:list):
    if len(alunos) == 0:
        print("Não existe nenhum aluno cadastrado")  
    else:
        for a in alunos:
            print("="*20)
            for k, v in a.items():
                print(f"{k} : {v}")
        
alunos = []
aluno = {}
controle = True

while controle:
    print("""
            ADICIONAR ALUNO     ( 1 )
            VISUALIZAR ALUNO    ( 2 )        
            ATUALIZAR ALUNO     ( 3 )      
            EXCLUIR ALUNO       ( 4 )          
            SAIR                ( 0 )                                    
          """)
    opcao = input("Digite a Opção: ")

    match opcao:
        case '1':
            print("Inserindo Aluno")
            nome = str(input("Nome do Aluno: ")).strip()
            matricula = int(input("Matricula do Aluno: "))            
            AdicionarAluno(nome, matricula)
        case '2':
            print("Listando Alunos")
            VerAlunos(alunos)
        case '3':
            print("Atualizando Aluno")
            matricula = int(input("Matricula do Aluno para atualizar: "))
            nome = str(input("Nome do Aluno : ")).strip()
            
            AtualizarAluno(matricula, nome)
        case '4':
            print("Removendo Aluno")
            matricula = int(input("Digite a Matricula do Aluno: "))
            RemoverAluno(matricula)
        case '0':
          controle = False
        case _:
            print('OPÇÃO INVALIDA')
else:
    print("Saindo do Sistema")