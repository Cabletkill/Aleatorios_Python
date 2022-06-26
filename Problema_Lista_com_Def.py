def impressao(c,p):
    lista01 = c
    lista02 = p
    print ('Lista = ',sorted(lista01.split()))
    print('Lista = ', sorted(lista02.split()))

def segunda_conta(c,p):
    valor= impressao(c,p)
    print('Segund valor = ',valor)

def terceiro_valor(c,p):
    print('Valor 01 = ',segunda_conta(c,p),'valor 02 =',impressao(c,p))

def entrada():
    c=(input('Digite o Conjunto 01: '))
    p=(input('Digite o Conjunto 02: '))
    impressao(c,p)


entrada()





