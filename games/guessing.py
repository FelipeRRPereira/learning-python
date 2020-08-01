print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

secret_number = 43
number_attempts = 3
roundNumber = 1

while roundNumber <= number_attempts:
    print("Tentativa", roundNumber, " de ", number_attempts)
    attempt_str = input("Digite o seu numero: ")
    print("Você digitou ", attempt_str)
    attempt = int(attempt_str)

    isCorrect = attempt == secret_number
    isBigger = attempt > secret_number
    isSmaller = attempt < secret_number

    if isCorrect:
        print("Você acertou!")
    else:
        if isBigger:
            print("Você errou! Valor informado maior que o número secreto.")
        elif isSmaller:
            print("Você errou! Valor informado menor que o número secreto.")

    roundNumber = roundNumber + 1

print("************")
print("Fim do jogo!")
print("************")
