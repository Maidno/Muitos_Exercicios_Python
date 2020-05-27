listagem = ('lápis', 1.75,
            'Borracha', 2.00,
            'lapizera', 4.00,
            'Compasso', 9.99,
            'Mochila', 140.90,
            'Caderno', 10.90)
for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<15}', end='')
    else:
        print(f'R${listagem[posicao]:>7.2f}')