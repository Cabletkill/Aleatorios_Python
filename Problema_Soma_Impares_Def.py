def impares(x,y):
    soma=0
    for i in range (x,y) or range (y,x):
           if not i%2==0:
                  soma = soma + i
    return soma

def prt(x,y):
    if impares(x,y)%2==0:
        print("Deu certo")
        print(impares(x,y))
    elif not impares(x,y)%2==0:
            print("Não deu certo")
            print(impares(x, y))



def main():
    x=int(input('Digite o primeiro numero:'))
    y=int(input('Digite o segundo numero:'))
    prt(x,y)
main()



