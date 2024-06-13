#Classe de idade (BOOLEAN - bool)
idade = int(input('Digite sua idade: '))

if(idade < 0 or idade > 120):
    print(f'Idade inválida')
elif (idade < 18):
    print(f'Infanto-Juvenil')
elif (idade < 60):
    print(f'Adulto')
else:
    print(f'Idoso')
