nome = input('Informe o seu nome: ')
idade = input('Informe a sua idade: ')

print(nome, idade)
print('teste',end=' ')
print(nome, idade, end='...\n') # \n é uma quebra de linha
print(nome, idade, sep='#') # sep é utilizado para criar o separador