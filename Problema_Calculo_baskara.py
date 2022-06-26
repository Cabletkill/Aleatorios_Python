import math
def entrada ():
    a=int(input('Digite o numero de A: '))
    b=int(input('Digite o numero de B: '))
    c=int(input('Digite o numero de C: '))
    resultado(a,b,c)

def delta(a, b, c):
    return (b ** 2) - 4 * (a) * (c)

def resultado(a,b,c):
    if delta(a, b, c) < 0:
        print('Delta menor que Zero')
    elif a==0:
        print('Conta invalida')
    else:
         raiz1= (-b + math.sqrt(delta(a, b, c)))/(2*a)
         raiz2 = (-b - math.sqrt(delta(a, b, c))) / (2 * a)
         print(raiz1)
         print(raiz2)
         print(delta(a,b,c))
entrada()
