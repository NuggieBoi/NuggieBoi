import random
import time

money = 250
reels = ("2", "9", "7")
spin = None

print("Welcome to the Slot Machines!")
time.sleep(0.5)
print(f"You have brought {money} dollars!")
time.sleep(0.5)
print("Well, it's bout' time you get gambling!")
print('')


def user_spin():
    global money
    global spin
    spin = input("Would you like to spin?(Y/N): ").lower()
    print('')


user_spin()


def game():
    global reels
    a = random.choice(reels)
    b = random.choice(reels)
    c = random.choice(reels)
    global spin
    global money
    if money <= 0:
        print("You ran out of money")
        return
    else:
        if spin == "y":
            print("You spent 25 dollars to spin")
            time.sleep(0.5)
            money -= 25
            print(f"{a} | {b} | {c}")
            time.sleep(1)
            if a == b and a == c:
                money += 75
                print("We have a winner!")
                time.sleep(0.5)
                print('')
                print(f"Now you have {money} dollars!")
                time.sleep(1)
                print('')
                again = input("Do you want to spin again?(Y/N): ").lower()
                print('')
                if again == "y":
                        game()
                else:
                    print("Okay, thanks for playing")
            else:
                print("You will get it next time!")
                time.sleep(0.5)
                print('')
                print(f"You now have {money} dollars")
                time.sleep(0.5)
                print('')
                again = input("Do you want to spin again?(Y/N): ").lower()
                print('')
                if again == "y":
                    game()
                else:
                    print("Okay, thanks for playing")
        elif spin == "n":
            return
        else:
            print("That's a invalid option(Y/N)")
            game()


game()
