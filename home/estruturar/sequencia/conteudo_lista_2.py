# Além de acessar vallores especícos utilizando o índice
# podemos acessar multiplos valores através do fatiamento.

# ex:
lista = [2, 3, 5, 7, 11]

# Imprimindo a lista fatiada do índice 0 à 2
print(lista[0:2])

# A mesma coisa acontece se fizer assim
print(lista[:2])

# se queremos excluir os dois primeiros valores usamos assim
print(lista[2:])
# ou assim
print(lista[-3:])

# tambem fatiar a lista para pegar elementos em um intervalo específico
print(lista[2:4])

# Tambem podemos adicionar um dado utilizando a função append()
lista2 = []
# Ao imprimir lista agora vai aparecer lista vazia
print(lista2)
lista2.append('zero')
# imprimindo nesse momento a lista recebeu o valor chamado 'zero'
print(lista2)
lista2.append('um')
# Nesse momento a lista recebeu o valor chamado 'um', imprimindo ['zero', 'um']
print(lista2)


# a função append so pode inserir um elemento por vez, se quisermos inserir mais podemos usar a função extend()
lista2.extend(['dois', 'tres'])
# ou
lista2 += ['quatro', 'cinco']
# ou multiplicar lista
lista2 *= 2

# imprimindo lista
print(lista2)

# podemos remover por posição
lista2.pop(11)

# podemos remover tudo com
# lista2.clear()

# podemos remover por nome
lista2.remove('cinco')

# imprimindo lista
print(lista2)

# isso é possivel porque as listas são mutáveis

# para imprimir o conteudo de uma lista posso usar o lçao for

for valor in lista2:
    print(valor)
