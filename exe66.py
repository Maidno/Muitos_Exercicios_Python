soma = cont = 0
while True:
    numero = int(input('Digite um valor [888 para parar]: '))
    if numero == 888:
        break  # como o break eu consigo interrope o fluxo do laço a qualquer momento
    cont += 1
    soma += numero
print(f'A soma dos {cont} valores foi {soma}!')

