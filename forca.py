def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while not acertou and not enforcou:

        chute = input("Digite uma letra: ")

        for letra in palavra_secreta:
            if(chute == letra):
                print(chute)

        print("Jogando ...")

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
