from random import randint


def guessComp(maxNum: int):
    randomInt = randint(0, maxNum)
    while True:
        userInput = input("\nGuess the number (e for exit): ")

        if userInput == "e":
            break

        if not userInput.isnumeric():
            print("Invalid Input: User input should be e or numeric.")
            continue

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

if not maxNum.isnumeric() or int(maxNum) < 0:
    raise Exception("Max num should be numeric and >= 0.")

guessComp(int(maxNum))
print()
