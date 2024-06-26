from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title('Exemplo de Widgets')

valores = ('segunda', 'terça', 'quarta', 'quinta', 'sexta')

combo_box = Combobox(janela, values=valores, state='readonly')
combo_box.pack(padx=200, pady=100)

progress_bar = Progressbar(janela, orient='horizontal', length=200, mode='indeterminate')
progress_bar.pack()
progress_bar.start(100)

sizegrip = Sizegrip(janela)
sizegrip.pack(anchor=SE,padx=3, pady=3, expand=True )

janela.mainloop()