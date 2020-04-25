from random import randint

computador = randint(0,5) # FAZ o computador sortear numeros entre 0 e 5

jogador = int(input('Digite um numero: '))

if jogador == computador:
    print('Você venceu !')
else:
    print('VocÊ perdeu! , eu pensei no número {} e não no {}'.format(computador,jogador))

