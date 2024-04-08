
urna ={
    "Rolando Lero (171)": 0,
    "Chaves (8)"        : 0,
    "Madruga (12)"      : 0,
    "Kiko (9)"          : 0,
    "Nulos"             : 0,
    "Brancos"           : 0,
}
controle = True
while controle:
    print("""
            Rolando Lero   (171)
            Chaves         ( 8 )        
            Madruga        ( 12)      
            Kiko           ( 9 )          
            Nulos          ( 0 )             
            Brancos"           
          """)
    voto = input("Escolha um(a) candidato(a): ")    
    if voto.lower() == "encerrar":
        controle = False
    else:
        match voto:
            case "171":
                urna["Rolando Lero (171)"] = urna["Rolando Lero (171)"]+1
            case "8":
                urna["Chaves (8)"] = urna["Chaves (8)"]+1
            case "12":
                urna["Madruga (12)"] = urna["Madruga (12)"]+1
            case "9":
                urna["Kiko (9)"] = urna["Kiko (9)"]+1
            case "0":
                urna["Brancos"] = urna["Brancos"]+1
            case _:
                urna["Nulos"] = urna["Nulos"]+1
print("Resultado das Eleições")
for chave in urna:
    print(chave, urna[chave], sep=": ")   