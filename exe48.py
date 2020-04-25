soma = 0
cont = 0
for contador in range(1, 50009, 2):
    if contador % 3 == 0:
        soma = soma + contador
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))