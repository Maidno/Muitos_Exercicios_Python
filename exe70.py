total = totalProdutosMil = menor = contador = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    contador += 1
    total += preco
    if preco > 1000:
        totalProdutosMil += 1
    if contador == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra for R${total:.2f}')
print(f'Temos {totalProdutosMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')