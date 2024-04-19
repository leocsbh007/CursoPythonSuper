import tkinter as tk

def btn_click():
    label.config(text="Botão Clicado")
    
janela = tk.Tk()

janela.title("Aula Tkinter")
janela.geometry('300x300')

label = tk.Label(janela, text="Isto é um Rotulo", font=("Arial", 12), fg="Red")
label.place(x=0, y=50)

label1 = tk.Label(janela, text="Isto é um Rotulo", font=("Arial", 12), fg="Red")
label1.place(x=10, y=70)


btn = tk.Button(janela, text="Clique Aqui", command=btn_click)
btn.place(x=30, y=90)


janela.mainloop()



