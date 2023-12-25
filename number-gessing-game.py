import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    attempts = 0
    while True:
        guess = input("Enter your guess (or 'q' to quit): ")
        
        if guess.lower() == 'q':
            print(f"The secret number was {secret_number}. Better luck next time!")
            break
        
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")
            continue
        
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try guessing a higher number.")
        elif guess > secret_number:
            print("Too high! Try guessing a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break

# Start the game
number_guessing_game()
