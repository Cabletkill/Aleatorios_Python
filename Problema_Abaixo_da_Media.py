def entrada():
    x=int(input("Quantos elementos tera o vetor?: "))
    print()
    func01(x)

def func01(x):
    soma = 0
    lista = []
    for i in range (1,x+1):
        j=float(input(f"Digite o {i}º numero:"))
        lista.append(j)
        soma  =  soma + j
    media = soma / x
    print()
    print('MEDIA DO VETOR = ',media)
    func02(lista, media)

def func02(lista, media):
    print()
    print('Elementos Abaixo da Média:')
    for i in range (0, len(lista)):
          if lista[i]<media:
              print(lista[i])

entrada()