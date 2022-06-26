def entrada():# entrada de dados
    x = int(input('Quantas pessoas voce ira digitar?:'))
    calc01(x)# chamada de função calc01(x)

def calc01(x):
    nome_lista = []
    idade_lista = []
    for i in range(1, x+1):
        print(f'Dados da {i}º pessoa:' )
        nome = input('Nome:')
        idade = int(input('Idade:'))
        nome_lista.append(nome)
        idade_lista.append(idade)
    cal02(nome_lista,idade_lista)

def cal02(nome_lista,idade_lista):
    nova = []
    troca_idade = 0
    for i in range(len(nome_lista)):# recebe a idade e devolve em formato de lista verificada
        c = idade_lista[i]
        if c > troca_idade: # demostra o resultado quem e o mais velho da lista
           troca_idade = idade_lista[i]
           nova = nome_lista[i]
    printa(nova)

def printa(nova):
    print("Pessoa mais velha:",nova)
entrada()