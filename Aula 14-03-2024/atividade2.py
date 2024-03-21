# ATIVIDADE PRÁTICA 2

# Crie uma função que receba um horário e imprima "Bom dia!" , "Boa tarde!" ou "Boa noite!" conforme o horário.
# "Bom dia!" - 6h as 12h
# "Boa tarde!" - 12h as 18h
# "Boa noite!" - 18h as 6h


def hora_do_dia(hora: int) -> str:
    if hora >= 6 and hora < 12:
        return 'Bom dia' 
    elif hora >= 12 and hora < 18:
        return 'Boa tarde'
    else:
        return 'Boa noite'
    
    
hora = int(input('Qual é a hora agora: '))
print(hora_do_dia(hora))
    
