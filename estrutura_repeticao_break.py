## while True:
##    numero = int(input("Advinhe o número que estou pensando: "))

##    if numero == 10:
##        print("Você acertou!")
##        break
    
##    print(numero)

## for numero in range (100):

##    if numero == 12:
##        break

##    print(numero, end= " ")

for numero in range (100):

    if numero % 2 == 0:
        continue

    print(numero, end= " ")