import random


def play():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    secret_number = random.randrange(1, 101)
    number_attempts = 0
    score = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    level = int(input("Defina o nível:"))

    if level == 1:
        number_attempts = 20
    elif level == 2:
        number_attempts = 10
    else:
        number_attempts = 5

    for roundNumber in range(1, number_attempts + 1):
        print("Tentativa {} de {}".format(roundNumber, number_attempts))
        attempt_str = input("Digite o seu numero: ")
        print("Você digitou ", attempt_str)
        attempt = int(attempt_str)

        if attempt < 1 or attempt > 100:
            print("Você deve digitar um número entre 1 e 100.")
            continue

        isCorrect = attempt == secret_number
        isBigger = attempt > secret_number
        isSmaller = attempt < secret_number

        if isCorrect:
            print("Você acertou e fez {:6.2f} pontos!".format(score))
            break
        else:
            if isBigger:
                print(
                    "Você errou! Valor informado maior que o número secreto."
                )
            elif isSmaller:
                print(
                    "Você errou! Valor informado menor que o número secreto."
                )
            lost_score = abs(secret_number - attempt) / 3
            score = score - lost_score

    print("************")
    print("Fim do jogo!")
    print("************")


if __name__ == "__main__":
    play()
