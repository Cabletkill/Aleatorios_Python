def main():
 x = int(input('Digite o numero: '))

 contador=0
 soma=0

 if x<0:
   print('Impossivel Calcular')

 while x>0:
  soma=soma+x
  contador=contador+1
  x = int(input('Digite o numero: '))
  if x<0:
     div=soma/contador
     print(f'Media={div:.2f}')
main()