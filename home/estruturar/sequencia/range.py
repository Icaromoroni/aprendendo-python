# range é um tipo de sequencia imutável de numeros, geralmente usados no looping de um numero especifico
# de vezes em um comando for ja que representa um intervalo.
# O comando range gera um valor contendo
# números inteiros sequenciais, obedecendo a sintaxe:
inicio = 0
fim = 4
sequencia = range(inicio, fim)
print('sequencia sem laço')
print(sequencia)
print('\n')


# para imprimir a sequencia e necessario um laço for
print('sequencia com laço')
for valor in sequencia:
    print(valor)
print('\n')

# Outra característica
# este comando é a de poder controlar o passo da sequência adicionando um terceiro parâmetro, isto é, a
# variação entre um número e o seu sucessor:

print('sequencia com laço controlando os passos de 2 em 2')
for valor in range(1, 10, 2):
    print(valor)
print('\n')
