from tkinter import *
from tkinter.ttk import *

janela =Tk()

janela.title('Teste Tree Viwe')
tree_view = Treeview(janela)

nomes = ["João", "Maria", "Pedro", "Ana", "Lucas", "Carla", "Mariana", "Paulo", "Laura", "Fernando"]
emails = ["joao@example.com", "maria@example.com", "pedro@example.com", "ana@example.com", "lucas@example.com", "carla@example.com", "mariana@example.com", "paulo@example.com", "laura@example.com", "fernando@example.com"]
telefones = ["123456789", "987654321", "999888777", "555444333", "777888999", "111222333", "999111222", "444555666", "888777666", "333222111"]



tree_view['columns'] = ('nome', 'email', 'telefone')

tree_view.column("#0", width=100, minwidth=100, anchor=CENTER)
tree_view.column("nome", width=150, minwidth=150, anchor=CENTER)
tree_view.column("email", width=150, minwidth=150, anchor=CENTER)
tree_view.column("telefone", width=150, minwidth=150, anchor=CENTER)

tree_view.heading('#0', text='ID')
tree_view.heading('nome', text='NOME')
tree_view.heading('email', text='EMAIL')
tree_view.heading('telefone', text='TEL')
i = 0
for nome in nomes:    
    tree_view.insert("", END, text=i+1, values=(nome, emails[i], telefones[i]))
    i += 1 

tree_view.pack()





janela.mainloop()