def entrada():
    x = int(input(" Quantas pessoas serao digitadas?:"))
    meio(x)
def meio(x):
    idadetotal = 0
    alturatotal = 0
    idade16 = 0
    lista = []
    for i in range (1, x+1):

        print(f'Dados da {i}º pessoa')
        nome = input('Nome:')
        idade = int(input('Idade:'))
        altura = float(input("Altura:"))

        idadetotal = idade + idadetotal
        alturatotal = alturatotal + altura

        if idade < 16:
           idade16 = idade16 + 1
           lista.append(nome)

    alturamedia = alturatotal/i
    mediaidade = ((idade16 / i)*100)
    print(f'Altura média:{alturamedia:.2f}')
    print(f'Pessoas com menos de 16 anos: {mediaidade:.2f}')
    print(lista)

entrada()