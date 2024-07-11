nome = "Barbara"
idade = 30
profissão = "Analista Financeiro"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Barbara", "idade": 30}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {name} Idade: {age}".format(name=nome, age=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.1f}")