def exibir_tarefa(lista:list):
  for item_lista in lista:
    codigo = item_lista ['codigo'] 
    descricao = item_lista ['descricao'] 
    categoria = item_lista ['categoria'] 
    concluida = item_lista ['concluida']    
  return codigo, descricao, categoria, concluida

tarefa = {
        'codigo': 1,
        'descricao': 'Aula do curso de Python da Infinity',        
        'categoria': 'trabalho',
        'concluida': 'não',
        }

lista_tarefas = []

lista_tarefas.append(tarefa)

print(exibir_tarefa(lista_tarefas))

