X = int (input('Digite a medida da glicose: '))

if X < 100:
    print('Classificacao: normal')
elif X < 140:
    print('Classificacao: Elevado')
else:
    print('Classificacao: Diabetes')
