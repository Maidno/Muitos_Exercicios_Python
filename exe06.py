import emoji
'''
Este foi o jeito que encotrei para resolver o exercicio

import math

n1 = int(input('Digite um numero: '))

dobro = n1 * 2
triplo = n1 * 3
raiz = math.sqrt(n1)

print('o dobro de {} e {}\n e o triplo e {}\n e a raiz quadra e {} '.format(n1,dobro, triplo,raiz))

'''
'''
Outra forma de fazer


n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n,d))
print('O triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f} '.format(n,t,n,r))
---------------------------------
bricadeiras com emoji
print(emoji.emojize(":thinking_face:"))

'''
n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O tripo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}'.format(n, (n*3), n, (n**(1/2))))