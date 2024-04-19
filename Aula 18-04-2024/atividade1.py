'''
ATIVIDADE PRÁTICA 1

Cadastro de Alunos (com exibição no terminal) Crie um
programa utilizando o Tkinter que permita ao usuário
cadastrar alunos. O programa deve solicitar o nome,
idade e nota do aluno por meio de caixas de entrada
(Entry) e exibir um botão para cadastrar. Ao cadastrar
um aluno, os dados devem ser exibidos no terminal.
'''

import tkinter as tk
    
    
def cadastro():
    # print(entry_nome.get())
    # print(entry_idade.get())
    # print(entry_nota.get())
    lbl_nome_output.configure(text=entry_nome.get())
    lbl_idade_output.configure(text=entry_idade.get())
    lbl_nota_output.configure(text=entry_nota.get())
    
    
janela = tk.Tk()

janela.title("Cadastro de Aluno")
janela.geometry('300x300')

lbl_nome = tk.Label(janela, text="Nome", font=("Arial", 12), fg="black")
lbl_nome.grid(row=0,column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)
lbl_nome_output = tk.Label(janela, text="", font=("Arial", 12), fg="black")
lbl_nome_output.grid(row=4,column=0)

lbl_idade = tk.Label(janela, text="Idade", font=("Arial", 12), fg="black")
lbl_idade.grid(row=1, column=0)
entry_idade = tk.Entry(janela)
entry_idade.grid(row=1, column=1)
lbl_idade_output = tk.Label(janela, text="", font=("Arial", 12), fg="black")
lbl_idade_output.grid(row=5,column=0)


lbl_nota = tk.Label(janela, text="Nota", font=("Arial", 12), fg="black")
lbl_nota.grid(row=2, column=0)
entry_nota = tk.Entry(janela)
entry_nota.grid(row=2, column=1)
lbl_nota_output = tk.Label(janela, text="", font=("Arial", 12), fg="black")
lbl_nota_output.grid(row=6,column=0)


btn = tk.Button(janela, text='Clique', command=cadastro)
btn.grid(row=3, column=0, columnspan=2)






janela.mainloop()
