'''
Este e um jeito de fazer este exercicio
import random

n1 = str(input('Digite o primeiro nome : '))
n2 = str(input('Digite o segundo nome : '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome : '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print((lista))

'''
from random import shuffle
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))

lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentação será :')
print(lista)