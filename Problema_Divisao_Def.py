def entrada():
    x= int (input("Quanto Casos Serão Analizados:"))
    func_div(x)

def func_div(x):
    for i in range (0,x):
        a=int(input("Entre com o Numerador:"))
        b=int(input("Entre com o Denominador:"))
        if b==0:
           print ('Divisão Impossivel')
        else:
            div=a/b
            print (div)
entrada()
'''
while not entrada()==0:#Cria um loop infinito da funcao entrada()
      print(1+1)
'''
