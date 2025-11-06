import random

print("🎯 Welcome to the Number Guessing Game!")
number_to_guess = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter your guess (1-100): ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        break