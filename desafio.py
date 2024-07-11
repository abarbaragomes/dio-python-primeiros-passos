## Desafio DIO: Criando um Sistema Bancário com Python
## Neste desafio são trabalhadas as seguintes operações: Depósito, Saque e Exibição de Extrato. Obs: considerando apenas 1 usuário.
## Sobre o depósito: Deve ser possível depositar valores positivos para a conta bancária. Não deve permitir depósito de valor negativo. E deve constar o valor depositado no extrato.
## Sobre saque: O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500 por saque. Em caso de saldo insuficiente, o sistema deve informar ao usuário. Todos os saques devem ser armazenados e constar no extrato.
## O sistema deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo R$ 1500.45

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input('Informe o valor a ser depositado: '))
        if deposito <= 0:
            print("Valor inválido. Refaça a operação!")
        else:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Depósito de R$ {deposito:.2f} efetuado com sucesso!")

    elif opcao == "2":
        if numero_saques >= LIMITE_SAQUES:
            print("Limite diário de saques atingido.")
        else:
            saque = float(input('Informe o valor a ser sacado: '))
            if saque > saldo:
                print("Saldo insuficiente em conta.")
            elif saque > limite:
                print("Saque não autorizado. O limite máximo por saque é de R$ 500")
            elif saque <= 0:
                print("Valor inválido. Refaça a operação!")
            else:
                saldo -= saque
                numero_saques += 1
                extrato += f"Saque: R$ {saque:.2f}\n"
                print(f"Saque de R$ {saque:.2f} efetuado com sucesso!")

    elif opcao == "3":
        print("\nExtrato:")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}\n")

    elif opcao == "4":
        print("Obrigado por utilizar nosso sistema bancário!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")