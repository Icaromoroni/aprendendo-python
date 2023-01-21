# Tuplas é uma lista imutável, ou seja, não pode ser alterada depois de criada.
# para definir uma tupla é necessario delimitar com parênteses '()'.

dias = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', ' sexta', 'sabado')
# imprimindo o tipo da variavel dias
print(type(dias))

# é possivel omitir os parênteses separando por vigula que ainda continua sendo uma tupla, na verdade
# não é o parenteses que define uma tupla e sim as virgulas. os parenteses são opcionais a nao ser que a tupla seja vazia
# Semelhante a lista dá pra criar uma tupla passando um tipo que pode ser interavel como uma string
# usando a função tuple()
texto = 'python'
# imprimindo tupla passando um tipo que
# pode ser iterável como uma string ou uma lista
print(tuple(texto))

# ou

lista = [1, 2, 3, 4]
print(tuple(lista))

# com a tupla nao é posivel usar o append e nem uma outra função para remover
# mas pode ser adicionado uma lista dentro de uma tupla
tupla = (1, 2, lista)
print(tupla)

# tupla são uteis geralmente para serem utilizada coleção de dados que nao possa ser alterados.
# as tuplas são usadas tambem para serem chave de dicionarios
