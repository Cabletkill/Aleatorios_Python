def entrada():
    x = int(input("Digite quantos caso serão analisados:"))
    func(x)


def func(x):
    resu = 0
    for c in range (1,x+1):
        y = float(input(f"Digite o {c}º caso:"))
        print(f'{c}º nota')
        if c == 1:
            soma = y * (2/10)
        elif c == 2:
            soma = y * (3/10)
        elif c == 3:
            soma = y * (5/10)
        resu = resu + soma
    print(f'Sua média final é {resu:2.2}')
entrada()