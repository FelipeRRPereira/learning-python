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

        hanged = error == 6
        hit = "_" not in correct_letter
        print(correct_letter)

    if(hit):
        print("You Won!!")
    else:
        print("Game Over!!")

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


if __name__ == "__main__":
    play()
