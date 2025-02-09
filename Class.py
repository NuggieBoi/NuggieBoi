import random


def main():
    f = open("demofile.txt", "r")
    f.readline()
    wins = int(f.readline())
    f.readline()
    loses = int(f.readline())
    f.readline()
    ties = int(f.readline())
    f.close()
    options = ["r", "p", "s"]
    running = True
    playing = True
    print(f"Looks like you have {wins} wins{loses} loses and {ties} ties")
    f = open("demofile.txt", "w")
    while playing:
        while running:
            user_choice = input("Rock, Paper, Or Scissors?(r,p,s) ").lower()
            if user_choice not in options:
                print("Pleas choose r, p or s")
            else:
                computer = random.choice(options)
                print(f"Com choose {computer} and you choose {user_choice}")
                if user_choice == computer:
                    print("You got a Tie!")
                    ties += 1
                elif user_choice == "r" and computer == "s":
                    print("You Won!")
                    wins += 1
                elif user_choice == "s" and computer == "p":
                    print("You Won!")
                    wins += 1
                elif user_choice == "p" and computer == "r":
                    print('You Won!')
                    wins += 1
                else:
                    print("You lost")
                    loses += 1
            running = False
        redo = str(input('Would you like to play again?(Y/N) ').lower())
        if redo == "y":
            running = True
        elif redo == "n":
            f.write("Wins = \n" + str(wins) + "\n")
            f.write("Loses = \n" + str(loses) + "\n")
            f.write("Ties = \n" + str(ties) + "\n")
            playing = False
            break
        else:
            print("Please choose Y or N ")

    f.close()


if __name__ == "__main__":
    main()
