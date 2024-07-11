MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input('Informe sua idade: '))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

elif idade == IDADE_ESPECIAL:
    print("Se fosse nos EUA seria permitido tirar a Carteira de Motorista.")

else :
    print("Ainda não pode tirar a CNH.")