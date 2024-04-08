print('Script para Menu de Controle de Tarefas')
print(25*'=-')
print(7*'=-','Controle de Tarefas',7*'=-')
print(25*'=-','\n')

tarefa1 = 0
feita1 = 0
tarefa2 = 0
feita2 = 0
tarefa3 = 0
feita3 = 0

aguarde = 0
tarefa_temporaria = 0

while True:
  print('O quê vamos Fazer Hoje???\n')
  print('Opção 1 - Visualizar Lista de Tarefas\n')
  print('Opção 2 - Adicionar Nova Tarefa\n')
  print('Opção 3 - Marcar Tarefa como Concluída\n')
  print('Opção 0 - Sair\n')
  print(25*'=-')

  opcao = int(input('Escolha sua Opção: '))

  if opcao == 1:
    print('Visualizando as Tarefas')
    if tarefa1 != 0 and tarefa2 != 0 and tarefa3 != 0:
      print(f'Tarefa - 1 : {tarefa1}')
      print(f'Tarefa - 2 : {tarefa2}')
      print(f'Tarefa - 3 : {tarefa3}')

    elif tarefa1 != 0 and tarefa2 != 0:
      print(f'Tarefa - 1 : {tarefa1}')
      print(f'Tarefa - 2 : {tarefa2}')

    elif tarefa1 != 0 and tarefa3 != 0:
      print(f'Tarefa - 1 : {tarefa1}')
      print(f'Tarefa - 3 : {tarefa3}')

    elif tarefa2 != 0 and tarefa3 != 0:
      print(f'Tarefa - 2 : {tarefa2}')
      print(f'Tarefa - 3 : {tarefa3}')

    elif tarefa1 != 0:
      print(f'Tarefa - 1 : {tarefa1}')

    elif tarefa2 != 0:
      print(f'Tarefa - 2 : {tarefa2}')

    elif tarefa3 != 0:
      print(f'Tarefa - 3 : {tarefa3}')

    else:
      print('Não existem tarefas no Banco')

    aguarde = int(input('Digite 9 para voltar: '))
    while True:
      if aguarde != 9:
        aguarde = int(input('Digite 9 para voltar: '))
      else:
        aguarde = 0
        break

  if opcao == 2:
    if tarefa_temporaria == 0:
      tarefa_temporaria = input('Digite a nova Tarefa: ')

    if tarefa1 == 0:
      tarefa1 = tarefa_temporaria
      tarefa_temporaria = 0
    elif tarefa2 == 0:
      tarefa2 = tarefa_temporaria
      tarefa_temporaria = 0
    elif tarefa3 == 0:
      tarefa3 = tarefa_temporaria
    else:
      print('Infelizmente o banco de Tarefas está cheio!!!')
      print('Marque como concluida para liberar espaço')


  if opcao == 3:
    print('Marcar Tarefa como Concluída')
    if tarefa1 != 0:
      feita1 = int(input(f'Marcar Tarefa - 1 : {tarefa1} como concluida digite 9 '))
      print(25*'=-')
      if feita1 == 9:
        print('Tarefa Concluida com Sucesso ')
        print('Foi retirada do Banco de Tarefas')
        tarefa1 = 0

    if tarefa2 != 0:
      feita2 = int(input(f'Marcar Tarefa - 2 : {tarefa2} como concluida digite 9 '))
      print(25*'=-')
      if feita2 == 9:
        print('Tarefa Concluida com Sucesso ')
        print('Foi retirada do Banco de Tarefas')
        tarefa2 = 0

    if tarefa3 != 0:
      feita3 = int(input(f'Marcar Tarefa - 3 : {tarefa3} como concluida digite 9 '))
      print(25*'=-')
      if feita3 == 9:
        print('Tarefa Concluida com Sucesso ')
        print('Foi retirada do Banco de Tarefas')
        tarefa3 = 0

    if tarefa1 == 0 and tarefa2 == 0 and tarefa3 == 0:
      print('Não existem tarefas no Banco')


  if opcao == 0:
    print('Você escolheu - Sair')
    print('Saindo do Sistema....')
    break