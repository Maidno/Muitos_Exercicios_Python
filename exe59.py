# o n1 recebe um número inteiro no qual eu estou pedido para o usuário digitar
n1 = float(input('Digite o primeiro valor: '))
# o n2 recebe um número inteiro no qual eu estou pedido para o usuário digitar
n2 = float(input('Digite o segundo valor: '))

#aqui estou inicializando a opcao
opcao = 0
while opcao != 5:

    print(''' 
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')

    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))

    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))

    elif opcao == 5:
        print('Finalizando..')

    else:
        print('Opção inválida. tente novamente')
print('Fim do programa')