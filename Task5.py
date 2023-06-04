import random

def guess_number():
    target_number = random.randint(0, 1000)
    attempts = 10

    print("Guess the number between 0 and 1000!")
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess < target_number:
            print("Greater than")
        elif guess > target_number:
            print("Less than")
        else:
            print("Congratulations! You guessed the number correctly!")
            return
        attempts -= 1

    print("Game over! You ran out of attempts. The target number was:", target_number)

# Run the game
guess_number()