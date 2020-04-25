import emoji

real = float(input('Quanto dinheiro você tem na carteira ? R$'))
dolar = real / 5.01


print(emoji.emojize(":money-mouth_face:" * 12))

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real,dolar))

print("----------------------------------------------------------------")

dolar2 = float(input('Dolar para Real :'))

real2 = dolar2 / 0.19

print('Com US${:.2f} você pode comprar R${:.2f}'.format(dolar2,real2))