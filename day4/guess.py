import random

def guessing_game():
    number_to_guess = random.randint(1, 10)  
    attempts = 5 
    print("Guess a number between 1 and 10:")
    for attempt in range(attempts):
            
            guess = int(input("Attempt :"))  # Get user input
            
            if guess == number_to_guess:
                print(f"You guessed the number in attemp",attempt+1)
                return
            elif guess < number_to_guess:
                print(f"Your guess is too low in attempt ",attempt+1)
            else:
                print(f"Your guess is too high in attempt",attempt+1)

    print("You did not guess the number. The number was:",number_to_guess,attempt+1)
guessing_game()