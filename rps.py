import random
import time
from subprocess import call

working = True
doing = True


def number_guess():
    global doing
    kevin = int(random.randrange(-1, 101))
    tries = 10
    print("Hello!")
    time.sleep(2)
    print("Welcome to the number guessing game!")
    time.sleep(1)
    print("So here are the rules: guess the number that kevin has in his mind and win!")
    time.sleep(1)
    print("See super easy!")
    time.sleep(1)
    print(f"Except there is one exception: you get only {tries} tries!")
    time.sleep(3)
    print("So enjoy your game!")
    print(" ")
    time.sleep(1)
    while doing:
        if tries == 0:
            print("Nice try. I hope you had fun! Have a good day!")
            doing = False
        else:
            user_guess = int(input("Enter a number 0-100   "))
            print("")
            if user_guess >= 101:
                print("please pick a number 0-100")
                print(" ")
            elif user_guess <= -1:
                print("please pick a number 0-100")
                print(" ")
            else:
                while True:
                    if user_guess == kevin:
                        print(f"You guessed the number with only {tries} tries left! Nice job!")
                        doing = False
                        break
                    elif user_guess <= kevin:
                        print("More than!")
                        tries -= 1
                        print(f"You have {tries} tries left")
                        print(" ")
                        break
                    elif user_guess >= kevin:
                        print("Less than!")
                        tries -= 1
                        print(f"You have {tries} tries left")
                        print(" ")
                        break


def rps():
    options = ("rock", "paper", "scissors")
    player = None
    computer = random.choice(options).lower()
    running = True

    while running:

        while player not in options:
            player = input("Enter a choice here (rock, paper, scissors)").lower()

        print(f"You chose: {player}")
        print(f"Computer chose: {computer}")

        if player == computer:
            print("It's a tie!")
            break
        elif player == "rock" and computer == "scissors":
            print("You broke the scissors. You won!")
            break
        elif player == "paper" and computer == "rock":
            print("You captured the rock. You won!")
            break
        elif player == "scissors" and computer == "paper":
            print("You cut paper into a million pieces! You won!")
            break
        else:
            print("You lost! )=")
            break

    play_again = input("Play again? (y/n)")
    if not play_again == "y":
        running = False
        print("Thanks for playing")
    else:
        rps()


print("Thanks for playing!")


def master_mind():
    import random

    def play_mastermind():
        colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']  # You can add more colors if you want
        code_length = 4  # You can change the code length

        def generate_secret_code():
            return random.sample(colors, code_length)

        def evaluate_guess(program_choice, user_choice):
            exact_matches = sum(a == b for a, b in zip(program_choice, user_choice))
            color_matches = sum(min(program_choice.count(Color), user_choice.count(Color)) for Color in colors)
            return exact_matches, color_matches - exact_matches

        def get_guess():
            while True:
                user_choice = input("Enter your guess (e.g., 'red blue green yellow'): ").lower().split()
                if len(user_choice) == code_length and all(Color in colors for Color in user_choice):
                    return user_choice
                else:
                    print("Invalid input. Please enter {} colors from: {}".format(code_length, colors))

        secret_code = generate_secret_code()

        print("Welcome to Mastermind!")
        print("Try to guess the secret code. The colors are: {}".format(colors))
        print("The code contains {} colors.".format(code_length))

        attempts = 0
        while True:
            attempts += 1
            your_guess = get_guess()
            exact, color = evaluate_guess(secret_code, your_guess)
            if exact == code_length:
                print("Congratulations! You guessed the code in {} attempts.".format(attempts))
                break
            else:
                print("Exact matches: {}, Color matches: {}".format(exact, color))

    if __name__ == "__main__":
        play = input("Do you want to play Mastermind? (yes/no): ").lower()
        if play == "yes":
            play_mastermind()
        else:
            print("Maybe next time!")


def user_game_choice():
    while working:

        print("What do you want to play? What mood of games are you? (master mind, rps, number guessing, card game)")
        choice = input("What game do you want to play?:  ")
        if choice == "rps":
            print("enjoy Rock paper scissors! (I hope you win!)")
            print(" ")
            time.sleep(3)
            rps()
        elif choice == "master mind":
            print("Enjoy your game of Master Mind!")
            print(" ")
            time.sleep(3)
            master_mind()
        elif choice == "number guessing":
            print("guess the number quickly!")
            print(" ")
            time.sleep(3)
            number_guess()
        elif choice == "card game":
            print(" ")
            call(["Python", "mon mon battle.py"])
        else:
            print("Please chose a valid game to play")


user_game_choice()
