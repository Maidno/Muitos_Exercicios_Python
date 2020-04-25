'''
#Condição Simples
nome = str(input('Qual é o seu nome ?'))
if nome == 'Máidno' and 'maidno' or 'máidno':
    print('Que nome podereso vocÊ tem!')
print('Tenha um bom dia, {}!'.format(nome))



'''

# Estrutura condicional composta
nome = str(input('Qual é o seu nome ?'))
if nome == 'Máidno':
    print('Que nome podereso vocÊ tem!')
elif nome == 'Karin' or nome == 'Tak' or nome == 'yuk':
    print('Você e um bot !')
else:
    print('Seu nome e bem normal!')
print('Tenha um bom dia, {}!'.format(nome))
