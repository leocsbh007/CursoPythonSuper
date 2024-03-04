# [PY-A01] Faça um programa em python que determine em duas variáveis (senha e email)
#  e que contenha uma senha e um email cadastrados antecipadamente, 
# em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição juntamente com a estrutura de condição para verificar se o email e a senha digitado pelo usuário é igual ao email e senha cadastrados antecipadamente. 
# E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue em um loop.


senha_cadastrada = "teste1"
email_cadastrado = "leo@gmail.com"

email = input("Insira o email: ")
senha = input("Insira a Senha de Acesso: ")
controle = True

while controle:
    if email == email_cadastrado:
        if senha == senha_cadastrada:
            controle = False
        else:
            print("Senha digita incorreta")
            email = input("Insira o email: ")
            senha = input("Insira a Senha de Acesso: ")    
    else:
        print("E-mail digitado incorreto")
        email = input("Insira o email: ")
        senha = input("Insira a Senha de Acesso: ")
else:
    print("Email e senha corretos")