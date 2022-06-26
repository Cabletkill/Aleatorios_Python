def medias_notas(x, y):

    somanotas=(x+y)/2
    return somanotas


x = int(input('Digite a Primeira Nota: '))
while x <= 0 or x > 10:
      print('Notas Invalidas')
      x = int(input('Digite a Primeira Nota: '))
y = int(input('Digite a Segunda Nota: '))
while y <= 0 or y > 10:
      print('Notas Invalidas')
      y = int(input('Digite a Primeira Nota: '))

print('MEDIA = {:.2f}'.format(medias_notas(x, y)))





