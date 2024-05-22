from tkinter import *

def exemplo():
    print(entry.get())


janela = Tk()

janela.title("Aula Tkinter")
janela.geometry('200x200')

label = Label(janela, text='Nome: ')
label.pack()
entry = Entry(janela)
entry.pack()
butao = Button(janela, text='Clique', command=exemplo)
butao.pack()

janela.mainloop()