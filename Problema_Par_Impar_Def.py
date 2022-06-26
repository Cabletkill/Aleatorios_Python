def entrada():
    x = int(input('Quantos numeros voce vai digitar?'))
    parimpar(x)
    print(test())

def parimpar(x):
    for i in range(1,x+1 ):
          y=int(input("Digite um numero:"))
          if y%2==0 and y>0:
             print('Numero par positivo')
          elif y%2==0 and y<0:
               print('Numero par negativo')
          if not y%2==0 and y>0:
                print('Numero impar positivo')
          elif not y%2==0 and y<0:
                print('Numero impar negativo')
          print('resultado do divisão = ',test2(x,y))
def test():
    return 'Encerrado'
def test2(x,y):
    return x%y

entrada()

