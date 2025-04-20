import random

def print_welcome_message():
    print("\n💖 Welcome Omotoke, Aduke aka Purple Rose Match Game! 💖")
    print("Choose a number between 1 and 10, and let the love vibes guide your fate. 💌\n")

def get_user_guess():
    return int(input("Enter your love number (1-10): "))

def give_love_message():
    love_messages = [
        "You are loved more than you know. 💕",
        "Your heart shines brighter than the stars. ✨",
        "Someone out there is thinking of you. 🌹",
        "Your smile can light up the darkest days. 😊",
        "You deserve endless hugs and warm cuddles. 🤗",
        "Your presence is pure magic. 🪄",
        "You're like a cozy blanket on a rainy day. ☔",
        "You're sweeter than chocolate and twice as lovely. 🍫",
        "Your kindness is a melody to the world. 🎵",
        "You're the missing piece to someone’s puzzle. 🧩"
    ]
    print(random.choice(love_messages))

def play_game():
    number_to_guess = random.randint(1, 10)
    tries = 1
    guess = get_user_guess()

    while guess != number_to_guess:
        give_love_message()

        if guess == -1:
            print("💌 Secret revealed: Your love number is", number_to_guess)
            guess = get_user_guess()
            continue

        if tries == 4:
            break

        guess = get_user_guess()
        tries += 1

    print_game_result(guess, number_to_guess, tries)

def print_game_result(guess, number_to_guess, tries):
    if guess == number_to_guess:
        print("💘 You found your perfect match in", tries, "tries! Love wins!")
    else:
        print("💔 Oops, not a match this time. The love number was", number_to_guess)

def ask_to_play_again():
    choice = input("Do you want to feel more love? (y/n): ")
    return choice.lower() == 'y'

def main():
    print_welcome_message()
    while True:
        play_game()
        if not ask_to_play_again():
            break
    print("\n💞 Love never ends... See you again soon! 💞")

# Run the game
main()
