Alcool=1
Gasolina=2
Diesel=3
Fim=4
print()
print(f'Qual produto o senhor deseja?')
print('1.Álcool = R$4,00')
print('2.Gasolina = R$5,00')
print('3.Diesel = R$6,00')
print('4.Fim')
def entrada_de_dados():
    x=int(input('Informe	um	codigo	(1,	2,	3)	ou	4	para	parar:'))
    calculando(x)

def calculando(x):
    somalitro1 = 0
    somalitro2 = 0
    somalitro3 = 0
    preco = 0
    preco1 = 0
    preco2 = 0
    preco3 = 0
    while not x == 4:
          if x == 1:
             print('Alcool')
             print()
             quantoslitros = int(input('Quantos Litros:'))
             somalitro1 = somalitro1+quantoslitros
             preco1 = somalitro1 *4.00
          elif x == 2:
               print('Gasolina')
               print()
               quantoslitros = int(input('Quantos Litros:'))
               somalitro2 = somalitro2+quantoslitros
               preco2= somalitro2 * 5.00
          elif x == 3:
               print('Diesel')
               print()
               quantoslitros = int(input('Quantos Litros:'))
               somalitro3=somalitro3+quantoslitros
               preco3 = somalitro3*6.00
          elif x > 4:
              print('Digite um codigo Valido!')
          preco = preco1+preco2+preco3
          x=int(input('Informe	um	codigo	(1,	2,	3)	ou	4	para	parar:'))
    put(somalitro1,somalitro2,somalitro3,preco)

def put(somalitro1,somalitro2,somalitro3,preco):

    print('Alcool:',somalitro1)
    print('Gasolina:',somalitro2)
    print('Diesel:',somalitro3)
    print ('Valor total gasto R$',preco)

entrada_de_dados()