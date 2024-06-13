#Notas bimestrais, media e aprovação de um aluno
nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if (media < 0 or media > 10):
    print(f'A sua média foi: {media:.1f}. Média Inválida')
elif (media < 7):
    print(f'Reprovado com média {media:.1f}!')
elif (media < 10 ):
    print(f'Aprovado com média {media:.1f} !')
else:
    print(f'Aprovado com  distinção!')
