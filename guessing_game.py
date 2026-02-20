import random

def guessing_game():
    numberToGuess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Guess the number between 1 and 100!")

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess > numberToGuess:
            print("Too high!")
        elif guess < numberToGuess:
            print("Too low!")
        else:
            print(f"Congratulations! You guesssed the number in {attempts} attempts!")
            break

guessing_game()