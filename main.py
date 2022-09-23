import random

palavras = ["Copo", "Orelhas", "Chocolate", "Pescador", "Notebook", "Lápis"]

palavras = random.choice(palavras)

tentativa = 0

chances = 3

letras_escolhidas = []

estado_atual = ["_"] * len(palavras)

print("Bem Vindo ao jogo da forca!")
print("O seu objetivo é acertar a palavra secreta!")
print("Lembre-se de inserir 1 letra por vez!")

while tentativa < chances:
    letra = input("\n\nQual letra você quer tentar?")
    while letra in letras_escolhidas:
        print("Erro!")
        print("\nVocê ja tentou essa letra!")
        letra = input("\n\nQual letra você quer tentar?")
    letras_escolhidas.append(letra)

    if letra in palavras:
        print("Parabéns, você acertou a letra!")
        for i in range(len(palavras)):
            if letra == palavras[i]:
                estado_atual[i] = letra
    else:
        print("Que pena você errou!")
        tentativa = tentativa + 1
    print("Você ja fez ",tentativa," e ainda tem ",tentativa - chances, "restantes!")
    print("Este é o estado atual:")
    print(estado_atual)
    print("As letras que você tentou são:")
    for i in letras_escolhidas:
        print (i, end=" ")
if tentativa == chances:
    print("Você perdeu!")
    print("Acabaram suas chances!")
else:
    print("Parabens!!! \n Você ganhou!")
print("A pelavra era ",palavras,"!")    