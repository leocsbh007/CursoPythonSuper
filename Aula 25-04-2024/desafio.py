'''
# Utilizando tkinter e o ttk, criaremos um programa para gerenciar uma lista de tarefas: 
# Nesse programa precisamos: 
- Poder criar uma nova tarefa
- Tarefas classificadas por urgência, devem ser exibidas em uma Tree_View em ordem de urgência.
- [Urgente, importante, não importante]
- Botão para adicionar novas tarefas
- Visualizar as tarefas
- Concluir uma tarefa (e ela sair da lista)
'''
def atualiza_id (id_tarefa:int) -> int:
    return id_tarefa + 1



def cadastro():
    # print(entry_nome.get())
    # print(entry_idade.get())
    # print(entry_nota.get())
    name = entry_tarefa.get()      
    prioridade = combo_box.get()

    id_tarefa = len(tree_view.get_children())
    # Tratar se a lista esta vazia
    # last_id = (tree_view.get_children()[-1]) # Verifica o penultimo elemento da tree view para comparar com o ultimo      
    tree_view.insert('', END, text=id_tarefa+1, values=(name, prioridade))
    print(tree_view.get_children())

# Para Resolver o problema de prioriade
# def add_people():
#     name = entry_name.get()
#     email = entry_email.get()
#     id = len(tree_view.get_children())
#     last_id = (tree_view.get_children()[-1])
#     item =  tree_view.insert('', END, text=id+1, values=(name, email, '123'))
#     last_value = tree_view.index(last_id)
#     item2 = tree_view.item(last_id)
#     tree_view.move(item, "", last_value) # troca a ordem do penultimo valor com o último valor adicionado na lista.



from tkinter import*
from tkinter.ttk import*


janela = Tk()

janela.title('Lista de Tarefas')
tree_view = Treeview(janela)
janela.geometry('500x500')

lbl_tarefa = Label(janela, text="Tarefa", font=("Arial", 12))
lbl_tarefa.pack()

entry_tarefa = Entry(janela, width=50)
entry_tarefa.pack(padx=2, pady=5)

lbl_prioridade = Label(janela, text="Prioridade", font=("Arial", 12))
lbl_prioridade.pack()
valores = ('URGENTE', 'IMPORTANTE', 'NÃO IMPORTANTE')
combo_box = Combobox(janela, values=valores, state='readonly')
combo_box.pack(padx=20, pady=10)

btn_cadastro = Button(janela, text='Incluir', command=cadastro)
# lambda: [fun1(), fun2()]) 
btn_cadastro.pack()


tree_view['columns'] = ('tarefa', 'classificacao')
tree_view.column("#0", width=100, minwidth=100, anchor=CENTER)
tree_view.column("tarefa", width=150, minwidth=150, anchor=CENTER)
tree_view.column("classificacao", width=150, minwidth=150, anchor=CENTER)
tree_view.heading('#0', text='ID')
tree_view.heading('tarefa', text='TAREFA')
tree_view.heading('classificacao', text='CLASSIFICAÇÃO')


tree_view.pack()


janela.mainloop()