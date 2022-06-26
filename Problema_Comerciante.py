def entrada():
    x = int(input('Serao digitados dados de quantos produtos?:'))
    conta_func(x)


def conta_func(x):
    lista_venda = []
    lista_compra = []
    soma = 0
    soma2 = 0
    soma3 = 0
    for i in range(1, x + 1):
        print(f'Produto {i}ª:')
        nome = str(input("digite o nome do produto: "))
        compra = float(input("Preço de compra: "))
        venda = float(input("Preço de venda: "))
        valor = (venda / compra)
        lista_compra.append(compra)
        lista_venda.append(venda)
        if valor < 1.1:
            soma = soma + 1
        elif 1.1 < valor < 1.2:
            soma2 = soma2 + 1
        elif valor > 1.2:
            soma3 = soma3 + 1
    total = sum(lista_venda) - sum(lista_compra)
    impre(soma, soma2, soma3, lista_compra, lista_venda, total)


def impre(soma, soma2, soma3, lista_compra, lista_venda, total):
    print('Relatorio geral de Vendas e Compras:')
    print('Lucro abaixo de 10%:', soma)
    print('Lucro entre 10% e 20%:', soma2)
    print('Lucro acima de 20%: ', soma3)
    print('Valor total de compra:', sum(lista_compra))
    print('Valor total de venda: ', sum(lista_venda))
    print('Lucro total:', total)


entrada()
