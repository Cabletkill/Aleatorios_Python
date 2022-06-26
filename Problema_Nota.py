X=int(input('Digite a primeira nota: '))

Y=int(input('Digite a segunda nota: '))

soma =  (X+Y)/2

print(f"NOTA FINAL = {soma:.2}")
if soma > 7:
    print ('Aprovado')
elif soma < 7:
        print("Reprovado")

