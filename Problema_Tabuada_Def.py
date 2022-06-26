def main():
    x=int(input('Digite o numero da tabuada:'))
    tabuada(x)

def tabuada(x):
    for i in range (1,100+1):
        soma =x*i
        print(x,'x',i,'=',soma)

main()