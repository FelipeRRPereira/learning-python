import random


def play():

    print_welcome()
    secret_word = get_secret_word()
    correct_letter = initial_correct_letter(secret_word)

    hanged = False
    hit = False
    error = 0

    while(not hanged and not hit):

        attempt = input("Qual letra? ")
        attempt = attempt.strip().upper()

        if (attempt in secret_word):
            index = 0
            for letter in secret_word:
                if(attempt == letter):
                    correct_letter[index] = attempt
                index += 1
        else:
            error += 1

        hanged = error == 6
        hit = "_" not in correct_letter
        print(correct_letter)

    if(hit):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")

    print("************")
    print("Fim do jogo!")
    print("************")


def print_welcome():
    print("*********************************")
    print("** Bem vindo ao jogo de forca! **")
    print("*********************************")


def get_secret_word():
    archive = open('games/words.txt', 'r')
    words = []

    for line in archive:
        line = line.strip()
        words.append(line)

    archive.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


def initial_correct_letter(word):
    ["_" for letter in word]


if __name__ == "__main__":
    play()
