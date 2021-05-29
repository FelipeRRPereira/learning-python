import random


def play():

    print_welcome()
    secret_word = get_secret_word()
    correct_letter = initial_correct_letter(secret_word)
    print(correct_letter)

    hanged = False
    hit = False
    error = 0

    while(not hanged and not hit):
        attempt = input_attempt()

        if (attempt in secret_word):
            mark_correct_letter(secret_word, attempt, correct_letter)
        else:
            error += 1
            draw_hangman(error)

        hanged = error == 7
        hit = "_" not in correct_letter
        print(correct_letter)

    if(hit):
        print_won()
    else:
        print_game_over(secret_word)

    print_finish()


def print_welcome():
    print("****************************************")
    print("** Welcome to the Fruit Hangman Game! **")
    print("****************************************")


def print_finish():
    print("****************************************")
    print("**               Finish               **")
    print("****************************************")


def get_secret_word():
    words = []
    with open('games/words.txt', 'r') as archive:
        for line in archive:
            line = line.strip()
            words.append(line)

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


def input_attempt():
    attempt = input("What's the letter? ")
    return attempt.strip().upper()


def initial_correct_letter(word):
    return ["_" for letter in word]


def mark_correct_letter(secret_word, attempt, correct_letter):
    index = 0
    for letter in secret_word:
        if(attempt == letter):
            correct_letter[index] = attempt
        index += 1


def print_game_over(secret_word):
    print("Ohh no, you were hanged!")
    print("The secret word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def print_won():
    print("Congratulations, you won!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def draw_hangman(error):
    print("  _______     ")
    print(" |/      |    ")

    if(error == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(error == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(error == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(error == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(error == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(error == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (error == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    play()
