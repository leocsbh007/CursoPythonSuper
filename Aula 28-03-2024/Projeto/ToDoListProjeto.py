def criar_tarefa(cod: str, desc: str, cat: str) -> dict:
  tarefa = {
      'codigo': cod,
      'descricao': desc,
      'categoria': cat,
      'concluida': False,    
  }
  return tarefa
  
def exibir_tarefa(lista:list):  
  if len(lista) == 0:
    print ("Não existe tarefa!!!")
  else:
    print('='*30)
    for item_lista in lista:
      print(f'Codigo da Tarefa:    {item_lista ["codigo"]}')
      print(f'Descrição da Tarefa: {item_lista ["descricao"]}')
      print(f'Categoria da Tarefa: {item_lista ["categoria"]}')
      print(f'Status da tarefa:    {item_lista ["concluida"]}')
    print('='*30)

def concluir_tarefa(lista:list, cod: str):
  if len(lista) == 0:
    return "Não existe tarefa!!!"
  else:
    lista[int(cod)]['concluida'] = True
    return "Tarefa Concluida"
        

# Lista que contem as tarefas
tarefas = []
controle = True
while controle:
    print("""
            CRIAR TAREFA     ( 1 )
            EXIBIR TAREFAS   ( 2 )        
            CONCLUIR TAREFA  ( 3 )      
            EXCLUIR TAREFA   ( 4 )          
            SAIR             ( 0 )                                    
          """)
    opcao = input("Digite a Opção: ")
    
    match opcao:
        case '1':
          print('='*30)
          print('CRIAR TAREFA')
          codigo_tarefa = input('Entre com o codigo da Tarefa: ')
          descricao_tarefa = input('Digite a Descrição da Tarefa: ')
          categoria_tarefa = input('Entre com a categoria da Tarefa: ')
          tarefa = criar_tarefa(codigo_tarefa, descricao_tarefa, categoria_tarefa)
          tarefas.append(tarefa)   
          print('='*30)       
        case '2': 
          print('='*30)
          print('EXIBIR TAREFAS')
          exibir_tarefa(tarefas)
          print('='*30)
        case '3': 
          print('='*30)          
          print('CONCLUIR TAREFA')          
          print("Na lista abaixo, qual tarefa deseja concluir: ")
          exibir_tarefa(tarefas)
          codigo = input('Entre com o codigo da Tarefa: ')
          #print(concluir_tarefa(tarefas, codigo))
          print(tarefas[int(codigo)][tarefa['concluida']])
          print('='*30)
        case '4': 
          print('EXCLUIR TAREFA')
        case '0':
          controle = False
        case _:
          print('OPÇÃO INVALIDA')
else:
  # print(tarefas)
  print('Saindo do Sistema')
              




