x = int(input('Digite os valores das coordenadas X: '))
y = int(input('Digite os valores das coordenadas Y: '))


while not (x == 0) or (y == 0):

    if x > 0 and y > 0:
        print('QUADRANTE Q1')
        x = int(input('Digite os valores das coordenadas X: '))
        y = int(input('Digite os valores das coordenadas Y: '))
    elif x < 0 and y > 0:
        print('QUADRANTE Q2')
        x = int(input('Digite os valores das coordenadas X: '))
        y = int(input('Digite os valores das coordenadas Y: '))
    elif x < 0 and y < 0:
        print('QUADRANTE Q3')
        x = int(input('Digite os valores das coordenadas X: '))
        y = int(input('Digite os valores das coordenadas Y: '))
    elif x > 0 and y < 0:
        print('QUADRANTE Q4')
        x = int(input('Digite os valores das coordenadas X: '))
        y = int(input('Digite os valores das coordenadas Y: '))


print('Termino da conta')


