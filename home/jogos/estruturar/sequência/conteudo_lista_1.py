# Uma lista é uma sequencia mutavel que recebe balores dentro de colchetes '[]'.

# Essa lista tem 4 valores armazenados em indices que começam a partir da posição 0.
lista1 = [1, 2, 3, 4]
# leitura para alista acima
# lista1 = [posição 0 = 1, posição 1 = 2, posição 2 = 3, posição 3 = 4]

# Imprimindo a lista1
print(lista1)

# imprimindo por posições
# posição 0
print(lista1[0])


# posição 1
print(lista1[1])
# ou posição reversa
print(lista1[-3])

# posição 2
print(lista1[2])
# ou posição reversa
print(lista1[-2])

# posição 3
print(lista1[3])
# ou posição reversa
print(lista1[-1])

# se tentar imprimir a posição 4 irá dar erro do tipo "IndexError: list index out of range", pois a posição não existe na lista.
# posição 4
# print(lista1[4])

# A lista pode ser de qualquer tipo a lista a cima é do tipo int, agora vamos fazer uma do tipo str.

lista2 = ['python', 'java', 'c#']
print(lista2)
# imprimindo por posições
# posição 0
print(lista2[0])
# ou posição reversa
print(lista2[-3])

# posição 1
print(lista2[1])
# ou posição reversa
print(lista2[-2])

# posição 2
print(lista2[2])
# ou posição reversa
print(lista2[-1])

# Podemos também ter listas heterogêneas.

lista = [1, 2, 'python', 3.5, 'java']

# Criando lista com afunção list()
lista3 = list('python')

# imprimindo lista3
print(lista3)

# Utilidade da lista é diversa
# ex:

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezambro']
n = 1
while n < 4:
    mes = int(input('Escolha um mês (1-12): '))
    if 1 <= mes < 13:
        print(f'O mês é {meses[mes-1]}')
        n += 1
