# code 9
import random

random_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))

    if guess < random_number:
        print("Too low, try again.")
    elif guess > random_number:
        print("Too high, try again.")
    else:
        print("Congratulations! You guessed the number.")
        break
