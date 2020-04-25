import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

# lista em python se declara entre cochetes
lista = [n1, n2, n3 , n4]
escolhido = random.choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))