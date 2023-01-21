# Problema item a.
# Defina uma variável fora do seu for chamada maiorValor e a
# iguale ao primeiro elemento na lista. Dentro do seu for , percorra os elementos dentro de um if
# para substituir o valor encontrado caso seja maior do que o mesmo:

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 12, 3, 3, -52]
menorValor = maiorValor = lista[0]
listaPares = []
ocorrenciaItem1 = 0

for elemento in range(0, len(lista)):
    # condição para maior valor
    if maiorValor < lista[elemento]:
        maiorValor = lista[elemento]
    # problema b adicionando menor valor
    if menorValor > lista[elemento]:
        menorValor = lista[elemento]
    # probema c adicionando numeros pares
    if lista[elemento] % 2 == 0:
        listaPares.append(lista[elemento])
    # problema d verificando ocorrencias
    if lista[elemento] == lista[0]:
        ocorrenciaItem1 += 1
print(maiorValor)
print(menorValor)
print(f'Lista pares: {listaPares}')
print(f'Numeros de ocorrencias: {ocorrenciaItem1}')
