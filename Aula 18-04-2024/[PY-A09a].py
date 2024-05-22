import tkinter as tk



def change_label_text():

    label.config(text="Texto alterado!")



root = tk.Tk()

root.title("Janela de Exemplo")



label = tk.Label(root, text="Olá!", font=("Arial", 16))

label.pack()



button = tk.Button(root, text="Alterar Texto", command=change_label_text)

button.pack()



root.mainloop()