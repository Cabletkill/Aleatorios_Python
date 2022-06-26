def entrada():
    x = int(input('Quantos valores vai ter cada vetor:'))
    list01(x)

def list01(x):
    print('Digite os valores dos vetores A:')
    lista01 = []
    for i in range (1,x+1):
        j=int(input(f'{i}ºnumero:'))
        lista01.append(j)
    print('Digite os valores dos vetores B:')
    lista02 = []
    for i in range(1, x + 1):
        z = int(input(f'{i}ºnumero:'))
        lista02.append(z)
    recebe03(lista01, lista02, x)

def recebe03(lista01,lista02, x):

    listanova = []
    print('Vetor Resultante:')
    for i in range(0,x):
        a=lista01[i]
        b=lista02[i]
        soma = a + b
        listanova.append(soma)
    print(listanova)



entrada()