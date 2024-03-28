def mostar_dados(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

mostar_dados(nome='Leo', idade=45, cidade='BH')