from datetime import date

atual = date.today().year

# Dia 04 - 04 - 2020 / validação por sexo!
sexo = str(input('Qual é o seu sexo : ')).strip().upper().lower()
if sexo == 'feminino':
    print('VocÊ não pode se ALISTAR!')
elif sexo == 'masculino':
    nascimento = int(input('Ano de nascimento: '))
    idade = atual - nascimento
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    elif idade > 18:
        saldo = idade - 18
        print('Você ja deveria ter se alistado há {} anos'.format(saldo))