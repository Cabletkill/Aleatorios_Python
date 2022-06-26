def entrada():
    x = int(input("Digite o Valor de N:"))
    func(x)
def func(x):
    cont = 1
    for i in range(x, 0, -1):
        cont = cont*i
    print('Fatorial = ', cont)

entrada()