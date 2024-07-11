conta_normal = False
conta_universitaria = True

saldo = 2000
saque = 1500
cheque_especial = 450

## if conta_normal:
##    if saldo >= saque:
##        print("Saque realizado com sucesso!")
##    elif saque <= (saldo + cheque_especial):
##        print("Saque realizado com uso do cheque especial!")
##    else:
##        print("Não foi possível realizar o saque. Saldo insuficiente!")

## elif conta_universitaria:
##    if saldo >= saque:
##        print("Saque realizado com sucesso!")
##    else:
##        print("Saldo insuficiente!")
 
status_conta_universitaria = "Sucesso" if saldo >= saque else "Falha"
print(f'{status_conta_universitaria} ao realizar o saque!')

## else:
##    print("O sistema não reconheceu o seu tipo de conta. Entre em contato com o seu gerente!")