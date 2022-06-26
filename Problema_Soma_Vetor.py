import math
import matplotlib.pyplot as plt
def entrada ():
    x = int (input('Quantos numeropara digitar?:'))
    conta(x)
def conta(x):
    soma = 0
    lista = []
    lista01 = []
    for i in range (1, x+1):
        z=float(input(f"Digite o {i}º numero: "))
        lista.append(z)
        lista01.append(z)
        soma = soma + z
    media = soma / x
    print('Valores = ',sorted(lista))
    print('Soma = ',soma )
    print ('Media = ',media )
    #plt.scatter(lista,lista01)
    #plt.show()
entrada()