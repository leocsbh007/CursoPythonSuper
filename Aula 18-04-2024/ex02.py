from tkinter import *

def exemplo():
    print(entry.get())


janela = Tk()

label = Label(janela, text='Nome: ')
label.pack()
entry = Entry(janela)
entry.pack()
butao = Button(janela, text='Clique', command=exemplo)
butao.pack()

janela.mainloop()