import guessing
import hangman


def choose_game():
    print("*********************************")
    print("****** Escolha o seu jogo! ******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if jogo == 1:
        print("Jogando forca")
        hangman.play()
    else:
        print("Jogando adivinhação")
        guessing.play()


if __name__ == "__main__":
    choose_game()
