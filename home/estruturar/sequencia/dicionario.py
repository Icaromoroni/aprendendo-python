# Os dicionários pertencem ao tipo de mapeamento integrado e
# não sequenciais como as listas, tuplas e strings
# obeseve o codigo:

pessoa = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}

print(pessoa)

# Os dicionários são delimitados por chaves ({}) e suas chaves ('nome', 'idade' e 'cidade') por aspas. Já
# os valores podem ser de qualquer tipo. No exemplo acima, temos duas strings e um int.

# não é possivel acessar os valores de um dicionario pelo indice como nas listas
# por exemplo:
# o comando pessoa[0] ocorrerá o KeyError: 0
# deve ser acessada pela sua chave
print(pessoa['nome'])
print(pessoa['idade'])

# para adicionar algum elemento como o país, basta fazer:
pessoa['país'] = 'Brasil'
print(pessoa)

# como é necesssario acessa os elementos através de chave, pode se usada a função keys()
print(pessoa.keys())

# e seus valores com a função values()
print(pessoa.values())

# as chaves de um dicionario nao podem ser iguais, para não causar conflito
# somente valores imutaveis podem ser usados como chave,
# nenhuma lista ou dicionario pode ser usado

# se o o comando como esse disc = {[1,2,3]: ' valor'} vai dar um erro do tipo TypeError: unhashable type: 'list'

# As tuplas podem ser usadas com chave de dicionarios.
