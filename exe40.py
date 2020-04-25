nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print(media)

if media <= 5:
    print('Reprovado!')
elif media >= 7:
    print('Aprovado !')
elif 7 > media >= 5:
    print('Aluno de recuperação')