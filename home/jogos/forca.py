# Cabeçalho do jogo

print('-' * 30)
print('| Bem vindo ao Jogo da Forca |')
print('-' * 30)

# Palavra Secreta
palavra_secreta = 'banana'
letras_acertadas = ['_', '_', '_', '_', '_', '_']
erros = 0

# variáveis tipada para booleano para definir qual chute foi certo ou errado alterando seu valor para True
acertou = False
enforcou = False
print('Dica:\nFruta com 6 letras.')
print(letras_acertadas)
# adicionando o loop e sua condição
while not acertou and not enforcou:
    chute = input('\nQual a letra?\n')

    if chute.upper() in palavra_secreta.upper():
        posicao = 0
        # Adicionando o laço for
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[posicao] = letra
            posicao += 1
    else:
        erros += 1
    acertou = '_' not in letras_acertadas
    enforcou = erros == 6
    print(letras_acertadas, '\n')
if acertou:
    print('Você ganhou!!')
else:
    print('Você perdeu!')

print('Fim do jogo.')
