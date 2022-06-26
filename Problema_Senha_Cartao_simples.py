meucartao=int(input('Digite o Numero do Seu Cartao de Crédito:'))

cartaolido=1
encontreimeucartao = False
while cartaolido != 0 and not encontreimeucartao:
    cartaolido= int(input('Digite o Numero do Proximo Cartao de Crédito:'))
    if cartaolido == meucartao:
     encontreimeucartao = True
if encontreimeucartao:
    print('Eba')