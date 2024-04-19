'''
ATIVIDADE PRÁTICA 2

Calculadora Simples (com exibição no terminal)

Desenvolva uma calculadora simples utilizando o Tkinter
que permita ao usuário realizar operações matemáticas
básicas, como adição, subtração, multiplicação e divisão.
O programa deve exibir botões para os números e as
operações, e ao realizar o cálculo, o resultado deve ser

exibido no terminal.
'''
import tkinter as tk
   
def soma():    
    num1 = entry_num1.get().strip()
    num2 = entry_num2.get().strip()
    if num1.isdecimal() and num2.isdecimal():
        soma = int(num1) + int(num2) 
        print(f'Soma = {soma}')
        lbl_resultado.grid(row=4,column=0)
        lbl_resultado.config(text=soma)
   
def subtracao():
    num1 = entry_num1.get().strip()
    num2 = entry_num2.get().strip()
    if num1.isdecimal() and num2.isdecimal():
        subtracao = int(num1) - int(num2) 
        print(f'Subtração = {subtracao}')
        lbl_resultado.grid(row=4,column=1)
        lbl_resultado.config(text=subtracao)
    
janela = tk.Tk()

janela.title("Calculadora")
janela.geometry('300x300')

lbl_num1 = tk.Label(janela, text="1º Numero", font=("Arial", 12), fg="black")
lbl_num1.grid(row=0,column=0)
entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1)

lbl_num2 = tk.Label(janela, text="2º Numero", font=("Arial", 12), fg="black")
lbl_num2.grid(row=1, column=0)
entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1)

lbl_resultado = tk.Label(janela,text="", font=('Arial', 12), fg='black')
lbl_resultado.grid(row=4,column=0)


btn_soma = tk.Button(janela, text='Soma', command=soma)
btn_soma.grid(row=3, column=0)

btn_sub = tk.Button(janela, text='Subtração', command=subtracao)
btn_sub.grid(row=3, column=1)

janela.mainloop()
