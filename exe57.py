sexo = str(input('Digite o seu sexo [M/F] : ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. tente novamente : ')).strip().upper()[0]
print('Sexo {} aceito com sucesso'.format(sexo))