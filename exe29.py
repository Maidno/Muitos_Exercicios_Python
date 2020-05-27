from itertools import count

velocidade = float(input('Qual a velocidade do carro : '))

if velocidade >= 80.0:
    print('Você foi multado , ultrapassou o limite permitido!')
    print('A multa será R$7,00 por cada Km acima do limite')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('Você está dentro do limite permitido ! Parabens!')
