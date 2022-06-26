def  multiplica(a,b):
    cont =a*b
    return cont

x=float(input('digite um numero:'))
y=float(input('digite um numero:'))

print(multiplica(y, x))


while multiplica(x, y)<10:
    print('-'*30)
    x = float(input('digite um numero:'))
    y = float(input('digite um numero:'))
    if multiplica(x, y)>10:
       print(multiplica(y, x))
    else:
        print(multiplica(y, x))




