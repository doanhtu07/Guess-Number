from random import randint


def guessComp(maxNum: int):
    if maxNum < 0:
        raise Exception("Invalid maximum number: Should not < 0.")

    randomInt = randint(0, maxNum)
    while True:
        userInput = input("\nGuess the number (e for exit): ")

        if userInput == "e":
            break

        if not userInput.isnumeric():
            raise Exception("User input should be e or numeric.")

        userInputInt = int(userInput)

        if userInputInt == randomInt:
            print("You are right! Wow!")
            print()
            print("Follow up: Do you know the best strategy for this game?")
            break

        if userInputInt < randomInt:
            print("Number > Input")
        else:
            print("Number < Input")


print()
print("Let's start!")
maxNum = input("Max range you want to play: ")

if not maxNum.isnumeric():
    raise Exception("Max num should be numeric.")

guessComp(int(maxNum))
print()
