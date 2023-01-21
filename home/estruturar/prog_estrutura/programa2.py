# ENTRADA DE DADOS
# O Python possui uma função que captura a entrada de valores: a função input()

mensagem = input('Digite algo: ')
print("você digitou:", mensagem)

print('O tipo de sua mensagem é:')
print(type(mensagem))

# Por padrão a função input define a entrada de dados no tipo str
# Para definir o tipo de dados especifico que entram é necessario usar junto com o input as funções:
# definindo a entrada de um numero como inteiro:
numero = int(input('Digite o numero: '))
print('Você digitou o numero:', numero)

print('O tipo do numero digitado é')
print(type(numero))

# definindo a entrada como float:
numero = float(input('Digite o numero: '))
print('Você digitou o numero:', numero)

print('O tipo do numero digitado é')
print(type(numero))

# definindo a entrada como booleano:
numero = bool(input('Digite o numero: '))
print('Você digitou o numero:', numero)

print('O tipo do valor digitado é')
print(type(numero))
