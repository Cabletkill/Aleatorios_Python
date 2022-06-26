def entrada():
    x = int(input('Quantas pessoas voce vai digitar?:'))
    calc(x)

def calc(x):
    lista1 = []
    lista2 = []
    for i in range (1, x+1):
        print(f'Digite o nome, a primeira nota e a segunda nota do {i}º aluno:')
        nome = input('Nome:')
        nota01 = float(input("Primeira nota:"))
        nota02 = float(input("Segunda nota:"))
        media_nota = ((nota01 + nota02) / 2)
        lista1.append(media_nota)
        lista2.append(nome)
    imp(lista1, lista2)

def imp(lista1, lista2):
    print()
    print('Alunos Aprovados:')
    print()
    c = 0
    for i in range(len(lista1)):
        if lista1[i] >= 6:
           c = c + 1
           print(f'{c}º Aprovado :',lista2[i], f", Nota = {lista1[i]}")

entrada()