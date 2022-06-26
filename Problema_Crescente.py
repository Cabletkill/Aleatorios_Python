def main():

    x = int(input('Digite o numero: '))
    y = int(input('Digite o numero: '))
    print()

    if x > y:
        print('DECRESCENTE!')
    elif x < y:
        print('CRESCENTE!')
    elif x == y:
        print()

    while x!=y:
     x = int(input('Digite o numero: '))
     y = int(input('Digite o numero: '))
     print()

     if x > y:
        print('DECRESCENTE!')
        print()
     elif x < y:
        print('CRESCENTE!')
        print()
     elif x == y:
        print('igual')
main()