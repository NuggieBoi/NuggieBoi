# This is made by a 12-year-old dev.
# I worked hard on this game so enjoy(=
# PS, I don't care if you remix this or not

from Class import Cards
import time
import random
import sys
from subprocess import call

user_poke = None
ene_poke = None
card_choice = None
checking = True
telling = True
battling = True
display_turn = 1
turn = 0
end = 0
x = 0
y = 0

options = str(("a", "b", "c")).lower()

# make user Pokémon, (poke is short for  Pokémon)
poke = Cards("Tryo", 20, 3, 4, 1)
poke2 = Cards("Punky", 24, 2, 5, 2)
poke3 = Cards("Fresh", 18, 2, 3, 3)
player_cards = (poke, poke2, poke3)

# make enemy Pokémon, (ene is short for enemy)
ene = Cards("Tyanto", 20, 3, 4, 2)
ene2 = Cards("Square ninja", 14, 3, 5, 1)
ene3 = Cards("Aral", 22, 2, 4, 2)
enemy_cards = (ene.name, ene2.name, ene3.name)


# introduce the user to the game and chose their Pokémon
def intro():
    print("Hello!")
    time.sleep(1)
    print("Welcome to 'Mon-Mon Battle'!")
    time.sleep(1)
    print("Here you will: chose a mon mon, see its stats, and battle!")
    print("And make sure your mons dont miss!")
    time.sleep(2)
    print("This was made by a 12-year-old")
    time.sleep(2)
    print("So with that said, enjoy your game!")
    time.sleep(1)
    print("Chose from one of these three cards to fight with")
    time.sleep(2)
    print('')
    print(f"A. {poke.name} {poke.__dict__}")
    print('')
    print(f"B. {poke2.name} {poke2.__dict__}")
    print('')
    print(f"C. {poke3.name} {poke3.__dict__}")
    print('')
    time.sleep(2)
    print('')


intro()


# tell user about enemy and go to battle
def enemy_stats():
    global y
    enemy = str(random.choice(enemy_cards))
    print("It's time to battle!")
    time.sleep(1)
    print(f"You have encountered a {enemy}")
    while telling:
        if enemy == ene.name:
            y = 1
            print("Here are the enemies stats:")
            print(ene.__dict__)
            break
        elif enemy == ene2.name:
            y = 2
            print("Here are the enemies stats:")
            print(ene2.__dict__)
            break
        elif enemy == ene3.name:
            y = 3
            print("Here are the enemies stats:")
            print(ene3.__dict__)
            break
    time.sleep(3)
    # start the battle
    # could not make this into separate funcs. because it would not work \=
    print("its battle time!")
    print(" ")


# Get the user choice and makes sure it's in the options(A, B, C)
def user_choice():
    global x
    global checking
    global card_choice
    card_choice = str(input("What card you you want?(A, B, C)")).strip().lower()
    while card_choice in options:
        while checking:
            if card_choice == "a":
                x = 1
                time.sleep(1)
                print("Have fun with your " + poke.name)
                enemy_stats()
                checking = False
            if card_choice == "b":
                x = 2
                time.sleep(1)
                print("Have fun with your " + poke2.name)
                enemy_stats()
                checking = False
            if card_choice == "c":
                x = 3
                time.sleep(1)
                print("Have fun with your " + poke3.name)
                enemy_stats()
                checking = False
        return card_choice
    if card_choice not in options:
        print("Please pick from the options A, B, or C")
        time.sleep(1)
        print("")
        user_choice()


user_choice()


# ask the player if they want to play again
# it will also check if they chose Y or N
def loop():
    global end
    yn = ("Y", "N")
    again = None

    while again not in yn:
        while True:
            again = input("Would you like to play again?(Y/N): ").strip().upper()
            if again == "Y":
                call(["Python", "mon mon battle.py"])
                break
            elif again == "N":
                print("Thanks for playing!")
                end = 1
                sys.exit()
            if again not in options:
                print("Please chose a valid option(Y/N)")
                print('')
                time.sleep(1)
                break
            else:
                sys.exit()


# this allows the program/AI to chose and use a random Pokémon
# to add another enemy choice, simply add another if statement and increase y by one
while True:
    if y == 1:
        ene_poke = ene
    if y == 2:
        ene_poke = ene2
    if y == 3:
        ene_poke = ene3
    break

# this will allow the user to actually use the Pokémon that he/she chose
# to add another poke. simply add another if statement and change the x by one
while True:
    if x == 1:
        user_poke = poke
    if x == 2:
        user_poke = poke2
    if x == 3:
        user_poke = poke3
    break


# enemy will choose to attack or use its special
# will also allow enemy to miss
def enemy_turn():
    global display_turn
    global battling
    global turn
    while True:
        if ene_poke.health >= 1 and user_poke.health <= 0:
            print("You have lost the game. )=")
            loop()
            break
        if ene_poke.health <= 0 and user_poke.health >= 1:
            print("You have won the game!")
            print("Congrats!(=")
            loop()
            break
        if turn == 2:
            hit = random.randint(0, 3)
            if hit == 0:
                ene_poke.opponent_miss()
            else:
                ene_poke.opponent_special()
                user_poke.health -= ene_poke.special_power
                print(f"Your {user_poke.name} is now at {user_poke.health} health")
                break
        elif turn < 2:
            hit = random.randint(0, ene_poke.attack_chance)
            if hit == 0:
                ene_poke.opponent_miss()
                break
            else:
                ene_poke.opponent_attack()
                user_poke.health -= ene_poke.attack_power
                print(f"Your {user_poke.name} is now at {user_poke.health} health")
                break
        else:
            print("Its a tie!")
            loop()
            break


# battle the enemy and allows the Mon to miss
def battle():
    global end
    while True:
        if end == 1:
            sys.exit()
        else:
            break
    global display_turn
    global turn
    global battling
    turn = 0
    while battling:
        while True:
            if user_poke.health <= 0 and ene_poke.health >= 1:
                print("You have lost the game. )=")
                end = 1
                loop()
                battling = False
                break
            else:
                pass
            print(f"turn {display_turn}")
            action = str(input("Do you want to attack, or use special?: ")).strip().lower()
            time.sleep(0.5)
            while True:
                if action == "attack":
                    hit = random.randint(0, user_poke.attack_chance)
                    if hit == 0:
                        turn += 1
                        display_turn += 1
                        user_poke.miss()
                        print('')
                        enemy_turn()
                        break
                    else:
                        user_poke.attack()
                        ene_poke.health -= user_poke.attack_power
                        print(f"The enemy health is now: {ene_poke.health}")
                        time.sleep(1)
                        print(f"And your {user_poke.name}s health is: {user_poke.health}")
                        print('')
                        enemy_turn()
                        turn += 1
                        display_turn += 1
                        time.sleep(1)
                        print('')
                        break

                if action == "special" and turn >= 2:
                    user_poke.special()
                    hit = random.randint(0, 3)
                    if hit == 0:
                        user_poke.miss()
                        enemy_turn()
                        display_turn += 1
                        turn = 0
                    else:
                        time.sleep(1)
                        ene_poke.health -= user_poke.special_power
                        print(f"The {ene_poke.name}s health is now: {ene_poke.health}")
                        enemy_turn()
                        display_turn += 1
                        turn = 0
                        break

                if action == "special" and turn < 2:
                    print("You need to wait some turns before you can use that")
                    time.sleep(1)
                    print('')
                    break

                if not action == "attack" or "special":
                    print("Please choice a valid option(Attack, or Special)")
                    print('')
                    time.sleep(1)
                    break

                while True:
                    if user_poke.health <= 0 and ene_poke.health >= 1:
                        print("You have lost the game. )=")
                        loop()
                        battling = False
                        break
                    elif user_poke.health <= 0 and ene_poke.health <= 0:
                        print("Its a tie!")
                        loop()
                        battling = False
                        break
                    else:
                        break


battle()

if __name__ == "__main__":
    intro()
