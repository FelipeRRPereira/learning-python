import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

secret_number = random.randrange(1, 101)
number_attempts = 3
roundNumber = 1

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
        print("Você acertou!")
        break
    else:
        if isBigger:
            print("Você errou! Valor informado maior que o número secreto.")
        elif isSmaller:
            print("Você errou! Valor informado menor que o número secreto.")

    roundNumber = roundNumber + 1

print("************")
print("Fim do jogo!")
print("************")
