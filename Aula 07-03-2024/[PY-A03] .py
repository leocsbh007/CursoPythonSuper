# [PY-A03] Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.
# O programa deve fornecer as seguintes funcionalidades:
# Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.
# Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.
# Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrícula.
# O programa deve ser executado em um loop contínuo até que o usuário escolha sair.

# alunos = [{'nome':'Leonardo',
#             'matricula': 1234},
#             {'nome':'Jose',
#             'matricula': 5678}]
alunos=[]
aluno = {}
novoAluno = {}
count = False
controle = True
num_matricula = 0

while controle:    
    print('''
                     MENU
        1 - Para INSERIR um Aluno
        2 - Para REMOVER um Aluno pela Matricula
        3 - Para VIZUALIZAR um Aluno
        4 - Encerrar o programa  
            ''')
    print('='*50)
    opcao = input('Entre com a Opção: ')
    match opcao:
        case '1':
            #Para Inserir um aluno
            print('INSERINDO ALUNO')
            novoAluno.clear()  
            novoAluno['nome'] = input('Entre com o nome do Aluno: ')
            novoAluno['matricula'] = int(input('Entre com o numero de Matricula: '))
            count = False        
            for aluno in alunos:
                if aluno['matricula'] == novoAluno['matricula']:
                    print('='*50)
                    print('JA EXISTE ALUNO CADASTRADO COM ESTA MATRICULA')
                    print('='*50)
                    print()
                    count = True
            if count is not True:                
                alunos.append(novoAluno.copy())
                print(alunos)
                count = 0
        # Para REMOVER um Aluno pela Matricula
        case '2':            
            if len(alunos) == 0:
                print('='*50)
                print('NÃO EXISTE ALUNO CADASTRADO')
                print('='*50)
                print()
            else:
                # Para excluir um aluno
                num_matricula = int(input('Entre com o numero de Matricula: '))
                for aluno in alunos:
                    if aluno['matricula'] == num_matricula:
                        alunos.remove(aluno)
                        print(f"ALUNO {aluno['nome']}, EXCLUIDO COM SUCESSO")
                                      
                print('='*50)
        case '3':
            for aluno in alunos:
                print('='*25)
                print(f"Nome Aluno: {aluno['nome']}")
                print(f"Matricula do Aluno: {aluno['matricula']}")
        case '4':
            controle = False
        case _:
            print("Entre com uma Opção valida")
else:
    print('Encerrando o Programa')



