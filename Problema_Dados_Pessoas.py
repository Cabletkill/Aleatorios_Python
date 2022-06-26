def entrada():
    x = int(input('Quantas pessoas serao digitadas?:'))#entrada de quantidade de pessoas que serão digitadas
    altura_genero(x)

def altura_genero(x):#recebe a quantidade de pessoas a serem verificadas
    lista_altura = []
    lista_genero = []
    lista_media_m = []
    lista_media_f = []
    media_f = 0
    media_m = 0
    for i in range(1, x + 1):
        altura = float(input(f'Altura da {i}ª pessoa: '))#entrada da Altura
        genero = str(input(f'Genero da {i}ª pessoa: '))#entrada do Genero
        lista_altura.append(altura) # recebe o valor da altura e armazena em uma lista
        lista_genero.append(genero.lower()) # recebe a string genero e armazena em uma lista
        if genero == 'f':
           lista_media_f.append(altura)#retira a a str F ou f da lista genero e armazena em uma nova lista
           media_f = media_f + altura #recebe o valor da altura relacionado a string F e soma
        if genero == 'm':
            lista_media_m.append(altura)#retira a a str M ou m da lista genero e armazena em uma nova lista
            media_m = media_m + altura #recebe o valor da altura relacionado a string M e soma
    saida(lista_media_f, lista_media_m, media_m, media_f, lista_genero)#retorna os valores para def saida

def saida(lista_media_f, lista_media_m, media_m, media_f, lista_genero):
    print()
    print('Maior Altura Mulheres = ',max(lista_media_f))
    print('Maior Altura Homens = ',max(lista_media_m))
    print()
    print('Menor Altura Mulheres = ',min(lista_media_f))
    print('Menor Altura Homens = ',min(lista_media_m))
    print()
    print('Media Alturas Mulheres = ',media_f/lista_genero.count('f'))
    print('Media Alturas Homens = ',media_m/lista_genero.count('m'))
    print()
    print('Total de Mulheres = ',lista_genero.count('f'))
    print('Total de Homens = ',lista_genero.count('m'))
entrada()