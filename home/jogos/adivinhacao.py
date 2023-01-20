# Comando if, else e elif

# Esse progama de um jogo de adivinhação que será necessário utilizar os comandos
# anteriores e com a função condicional if

# Cabeçalho do jogo
print('-' * 30)
print('*   Jogo da adivinhação      *')
print('-' * 30)


numero_secreto = 42
# Entrada de dados
# variável = tipo(entrada de dados('valor digitado: '))
#chute = int(input('Digite um número: '))

# Estrutura de condição

'''if chute == numero:
    print('Você acertou')
else:
    print('Você errou :(')'''


# Comando com dica
'''if chute == numero_secreto:
    print('Você acertou!')
else:
    if chute > numero_secreto:
        print('Você errou! O seu chute foi maior que o número secreto')
    else:
        print('Você errou! O seu chute foi menor que o número secreto')'''

# Comando usando o elif

'''if chute == numero_secreto:
    print('Você acertou!')
elif chute > numero_secreto:
    print('Você errou! O seu chute foi maior que o número secreto')
elif chute < numero_secreto:
    print('Você errou! O seu chute foi menor que o número secreto')'''

# Melhorando o codigo ou refatorando

'''acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if acertou:
    print('Você acertou!')
elif maior:
    print('Você errou! O seu chute foi maior que o número secreto')
if menor:
    print('Você errou! O seu chute foi menor que o número secreto')'''

# Adicionando o WHILE enquanto há tentativas
total_de_tentativas = 5
rodada = 1
while rodada <= total_de_tentativas:
    if rodada != total_de_tentativas:
        print(f'Tentativa {rodada} de {total_de_tentativas}.')
    elif rodada == total_de_tentativas:
        print('Ultima tentativa!')
    chute = int(input('Digite seu número: '))
    print('Você digitou', chute)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if acertou:
        print('Parabéns você acertou!\n')
        break
    elif maior:
        print('Você errou! O seu chute foi maior que o número secreto\n')
    elif menor:
        print('Você errou! O seu chute foi menor que o número secreto\n')
    rodada += 1

print('Fim de jogo!')
