import random

def print_welcome_message():
    print("Welcome to the Number Guess Game!")

def get_user_guess():
    return int(input("Please guess a number between 1 and 10: "))

def check_proximity(guess, number_to_guess):
    if guess + 1 == number_to_guess or guess - 1 == number_to_guess:
        print("Your guess was within 1 of the number!")

def play_game():
    number_to_guess = random.randint(1, 10)
    tries = 1
    guess = get_user_guess()

    while guess != number_to_guess:
        if guess == -1:
            print("Cheat mode: the number is", number_to_guess)
            guess = get_user_guess()
            continue

        print("Sorry, wrong number.")

        if tries == 4:
            break
        elif guess < number_to_guess:
            print("Your guess was lower than the number.")
        else:
            print("Your guess was higher than the number.")

        check_proximity(guess, number_to_guess)

        guess = get_user_guess()
        tries += 1

    print_game_result(guess, number_to_guess, tries)

def print_game_result(guess, number_to_guess, tries):
    if guess == number_to_guess:
        print("🎉 Well done! You won in", tries, "tries.")
    else:
        print("❌ Sorry, you lose. The number was", number_to_guess)

def ask_to_play_again():
    choice = input("Do you want to play again? (y/n): ")
    return choice.lower() == 'y'

def main():
    print_welcome_message()
    while True:
        play_game()
        if not ask_to_play_again():
            break
    print("Game Over!")

# Run the game
main()
