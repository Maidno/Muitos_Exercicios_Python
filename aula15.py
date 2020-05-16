numero = soma = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 888:
        break
    soma += numero
#print('A soma vale {}'.format(s))
print(f'A soma vale {soma}') #Técnica de interpolação de Strings
