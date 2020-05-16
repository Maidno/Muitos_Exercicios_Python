print('Seguência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
TermoUm = 0
TermoDois = 1
print('X'*30)
print('{} > {}'.format(TermoUm, TermoDois), end='')
cont = 3
while cont <= n:
    TermoTres = TermoUm + TermoDois
    print(' > {}'.format(TermoTres), end='')
    TermoUm = TermoDois
    TermoDois = TermoTres
    cont += 1
print(' > FIM')
print('X'*30)