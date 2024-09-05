#Importing the libraries
import random
import time

# Function to generate a random number between 1 and 200
def generate_random_number():
    return random.randint(1, 200)

# Function to introduce the game and get the player's name
def intro():
    print("May I ask you for your name?")
    pname = input()
    print(f"{pname}, we are going to play a game. I am thinking of a number between 1 and 200.")
    time.sleep(0.5)
    print("Go ahead. Guess!")

# Function to handle the guessing game logic
def pick(number):
    guesses_taken = 0
    max_guesses = 6  # Maximum number of allowed guesses

    while guesses_taken < max_guesses:
        time.sleep(0.25)
        enter = input("Guess: ")

        try:
            guess = int(enter)  # Convert the input to an integer

            if 1 <= guess <= 200:  # Check if the guess is within the valid range
                guesses_taken += 1

                if guess < number:
                    print("The guess of the number that you have entered is too low.")
                elif guess > number:
                    print("The guess of the number that you have entered is too high.")
                else:
                    print(f"Good job! You guessed my number in {guesses_taken} guesses!")
                    return True  # Number guessed correctly

                if guesses_taken < max_guesses:
                    time.sleep(0.5)
                    print("Try Again!")

            else:
                print("Silly Goose! That number isn't in the range!")
                print("Please enter a number between 1 and 200.")

        except ValueError:
            print(f"I don't think that {enter} is a number. Sorry.")

    # If the number wasn't guessed within the allowed guesses
    print(f"Nope. The number I was thinking of was {number}.")
    return False

# Main function to control the game flow
def main():
    while True:
        number = generate_random_number()  # Generate a new number for each game
        intro()  # Introduce the game
        pick(number)  # Start the guessing game
        
        # Ask the player if they want to play again
        print("Do you want to play again? (yes/no)")
        play_again = input().strip().lower()

        # If the player does not want to play again, exit the loop
        if play_again not in ["yes", "y"]:
            break

# Entry point of the program
if __name__ == "__main__":
    main()
