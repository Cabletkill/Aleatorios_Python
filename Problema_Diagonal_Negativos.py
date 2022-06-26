def entrada():
    x = int(input("Qual a ordem da matriz?:"))
    calc(x)

def calc(x):
    nova = []
    for i in range(0,x):
        for j in range(0,x):
            elemento = int(input(f"Elemento[{i},{j}]:"))
            nova.append(elemento)
    diagonal = []
    calc02(nova, diagonal,x)

def calc02(nova, diagonal,x):
    soma = 0
    for i in range(0,len(nova),x):
          diagonal.append(nova[i])
          if nova[i] < 0:
             soma = soma +1
    printa(soma, diagonal)

def printa(soma,diagonal):
    print('Diagonal Principal:')
    print(diagonal)
    print(soma)

entrada()
