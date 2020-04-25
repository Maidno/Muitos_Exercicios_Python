print('{:=^40}'.format(' LOJAS M '))
preço = float(input('Preço das compras: R$'))
print(''' FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] a vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção ?'))
if opcao == 1:
    total = preço - (preço * 10 / 100)
elif opcao == 2:
    total = preço - (preço * 5 / 100)
elif opcao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc,parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final. '.format(preço, total))