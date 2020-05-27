import emoji

n1 = int(input('Digite um numero : '))
mut1 = n1 * 1
mut2 = n1 * 2
mut3 = n1 * 3
mut4 = n1 * 4
mut5 = n1 * 5
mut6 = n1 * 6
mut7 = n1 * 7
mut8 = n1 * 8
mut9 = n1 * 9
mut10 = n1 * 10

print(emoji.emojize(":money-mouth_face:" * 12)) # utilizando emoji para deixar legal
print('{} x {:2} = {}'.format(n1, 1, mut1))
print('{} x {:2} = {}'.format(n1, 2, mut2))
print('{} x {:2} = {}'.format(n1, 3, mut3))
print('{} x {:2} = {}'.format(n1, 4, mut4))
print('{} x {:2} = {}'.format(n1, 5, mut5))
print('{} x {:2} = {}'.format(n1, 6, mut6))
print('{} x {:2} = {}'.format(n1, 7, mut7))
print('{} x {:2} = {}'.format(n1, 8, mut8))
print('{} x {:2} = {}'.format(n1, 9, mut9))
print('{} x {:2} = {}'.format(n1, 10, mut10))