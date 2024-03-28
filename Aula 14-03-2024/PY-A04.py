'''
[PY-A04] Desenvolva um programa em Python que permita ao usuário digitar várias notas. Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno. Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.
'''


'''
FUNÇÃO PARA CALCULAR A MEDIA DE NOTAS
INPUT - LISTA DE NOTAS DO TIPO FLOAT
OUTPUT - MEDIA DAS NOTAS DO TIPO FLOAT
'''
def calcular_media(notas:float) -> float:
    media = 0
    media = sum(notas)/len(notas)
    return media

'''
FUNÇÃO PARA MOSTRAR A SITUAÇÃO DE UM ALUNO
INPUT - MEDIA DAS NOTAS DO TIPO FLOAT
OUTPUT - MENSAGEM COM A SITUAÇÃO DO ALUNO
'''
def verificar_situacao(media:float) -> str:
    situacao = ''
    if media < 7.0:
        situacao = "Reprovado"
    elif media >= 7.0 and media < 10.0:
        situacao = "Aprovado"
    else:
        situacao = "Parabéns, sua média é 10"
    return situacao

notas = []
nota = 0
controle = True
sair = 0
while controle:
    if controle is True:        
        nota = float(input("Entre com as notas do Aluno: "))
        if nota > 10:
            print("==== ERRO ===")
            print("Sitema só aceita notas menores que 10")
            print("==== ERRO ===")
            nota = float(input("Entre com as notas do Aluno: "))
        notas.append(nota)
    sair = input("Deseja incluir outra nota?(s/n): ").upper()    
    if sair == 'N':
        controle = False
else:
    media = calcular_media(notas)
    print("="*30)
    print("Media", media)
    print("Situação do Aluno")
    print (verificar_situacao(media))
    print("="*30)    
    print("Saindo do Sistema!!!")