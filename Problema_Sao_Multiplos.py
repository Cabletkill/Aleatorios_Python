def main():
   ##inicio do programa com duas variaveis
    X=int(input('Digito o primeiro numero: '))
    Y=int(input('Digito o Segundo numero: '))

    ##antes de efetuar a condição if fiz o teste do resultado, tire os # para efetuar a conta dentro do programa.
    ##soma=X//Y
    ###print('Resultado:', soma)

    ##a condição IF testa se um dos dois resultados tem a sobra zero em uma das divizões caso sim ele valida o multiplo.
    if X%Y==0 or Y%X==0:
        print("São multiplos!")
    else:
        print("Não são multiplos!")

main()
