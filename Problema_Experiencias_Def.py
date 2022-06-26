def entrada():
    x= int (input("Quantos casos de teste serao digitados?: "))
    print('S=Sapo', "C=Coelho", 'R=Rato')
    func(x)

def func (x):
    '''
    :param x: recebe o valor entrada//quantidade de casa a serem analisados
    :return: retorna o resultado da pesquisa
    '''
    cont=0
    contr=0
    conts=0
    contc=0
    for i in range (1,x+1):
        A=int(input("Quantidade de cobaias: "))
        B=(input("Tipo de cobaia: "))
        cont = cont +A
        if B=='c' or B=='C':
           contc=contc+A
        elif B=="r" or B=='R':
             contr = contr + A
        elif B=='s' or B=='S':
             conts=conts + A
    print ('RELATORIO FINAL:')
    print()
    print(f'Total: {cont} cobaias ')
    print()
    print('Total de coelhos',contc)
    print('Total de ratos',contr)
    print('Total de sapos',conts)
    print()
    print('Percentual  de coelhos',((contc/cont)*100))
    print('Percentual  de ratos',((contr/cont)*100))
    print('Percentual  de sapos',((conts/cont)*100))

entrada()