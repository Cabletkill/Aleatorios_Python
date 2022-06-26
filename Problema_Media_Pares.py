def entrada ():
    x = int(input('Quantos elementos vai digitar?:'))
    func(x)

def func(x):
    somapar = 0
    somaimpar = 0
    contpar = 0
    contimp = 0
    for i in range(1,x+1):
        j = int(input(f'Digite o {i}º numero:'))
        if j % 2 == 0:
            contpar = contpar + 1
            somapar = somapar + j
        elif not j % 2 == 0:
            contimp = contimp + 1
            somaimpar = somaimpar + j
    imprime(contpar, contimp, somapar, somaimpar)

def imprime(contpar, contimp, somapar , somaimpar):
    if contpar == 0:
       print('Não houve numeros pares')
    elif contpar > 0:
       resultado_par = somapar / contpar
       print('Media numeros pares:',resultado_par)
    if contimp == 0:
        print('Não houve numeros impares:')
    elif contimp > 0:
        resultado_imp = somaimpar / contimp
        print('Media numeros impares:',resultado_imp)
entrada()