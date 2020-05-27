
'''
Primeiro Exemplo

nome = str(input('Qual é seu nome? '))
if nome == 'Maidno':
    print('Então você é o Guerreiro onisciente !')
print('O que você quer ? {}'.format(nome))

'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 7.0:
    print('Sua média foi boa ! PARABENS!')
else:
    print('Estude mais !')
