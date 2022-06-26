X= int(input('Digite a quantidade de minutos: '))

if X < 50:
    print('Valor a pagar: R$ 50.00')
elif X > 50 :
     soma= ((X-50)*2)+50
     print(f'Valor a pagar: R${soma}')
