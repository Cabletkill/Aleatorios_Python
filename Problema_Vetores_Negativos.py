import matplotlib.pyplot as plt
def entrada ():
    x=int(input('Quantos numero voce vai digitar? :'))
    lista(x)
def lista(x):
    lista=[]
    lista02=[]
    for i in range (1, x+1):
        z=int(input(f'Digite o {i}º numero:'))
        if z < 0:
            lista.append(z)
        elif z > 0:
             lista02.append(z)
    print('Lista Negativa =',sorted(lista))
    print('Lista Positiva =',sorted(lista02))
    a = lista02
    b = lista
    return a,b
def listinha(a,b):

    print('Lista 01 Negativa =', sorted(a))
    print('Lista 02 Positiva =', sorted(b))

    plt.scatter(sorted(a),sorted(b))
    plt.show()
entrada()
