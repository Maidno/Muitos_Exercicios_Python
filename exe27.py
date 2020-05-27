nome = str(input('Digite o seu nome : ')).strip()
separe = nome.split()
print('Seu primeiro nome é {}'.format(separe[0]))
print('Seu ultimo nome é {}'.format(separe[len(separe)-1]))
