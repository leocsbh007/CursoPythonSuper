import tkinter as tk
from tkinter import ttk

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Janela Principal")
        self.geometry("400x200")

        self.button = ttk.Button(self, text="Abrir Janela Modal", command=self.abrir_janela_modal)
        self.button.pack(pady=20)

    def abrir_janela_modal(self):
        # Desabilita a janela principal para bloquear interações
        self.wm_attributes("-disabled", True)

        # Cria a janela modal
        self.janela_modal = tk.Toplevel(self)
        self.janela_modal.title("Janela Modal")
        self.janela_modal.geometry("300x150")

        # Adiciona widgets à janela modal
        self.label = ttk.Label(self.janela_modal, text="Esta é uma janela modal.")
        self.label.pack(pady=20)

        # Botão para fechar a janela modal e reativar a janela principal
        self.fechar_botao = ttk.Button(self.janela_modal, text="Fechar", command=self.fechar_janela_modal)
        self.fechar_botao.pack(pady=10)

    def fechar_janela_modal(self):
        # Reativa a janela principal
        self.wm_attributes("-disabled", False)

        # Fecha a janela modal
        self.janela_modal.destroy()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()