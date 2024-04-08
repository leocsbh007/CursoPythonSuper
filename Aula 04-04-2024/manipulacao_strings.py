def inverter_string(string: str) -> str:
    '''
    Recebe uma string e retorna o seu valor invertido
    '''
    string_invertida = string[::-1]    
    return string_invertida

def contar_palavras(nome: str) -> int:
    '''
    Conta quantas plavras tem uma stringa
    '''
    contagem = 0    
    contagem = len(nome.split())    
    return contagem

def palindromo(nome:str) -> str:
    pass
    