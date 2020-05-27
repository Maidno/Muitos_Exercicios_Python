while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break
    print('X' * 30)
    for contador in range(1, 11):
        print(f'{numero} x {contador} = {numero*contador}')
    print('X' * 30)
f