import random

number = random.randint(1, 100)
attempts = 7

print(" Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("You have 7 attempts to guess it.\n")

for i in range(attempts):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print(" Congratulations! You guessed the correct number.")
        print("Attempts used:", i + 1)
        break
    elif guess > number:
        print("Too High!")
    else:
        print("Too Low!")

    print("Attempts remaining:", attempts - (i + 1))
else:
    print("\n You failed! The correct number was:", number)