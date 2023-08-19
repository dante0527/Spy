from random import randint, choice
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_n_players(num):

    while True:

        try:
            assert int(num) >= 3
            return int(num)
        
        except ValueError:
            clear()

            print("Input must be a number.")
            num = input("Enter number of players: ")
            pass

        except AssertionError:
            clear()

            print("Must have at least 3 players")
            num = input("Enter number of players: ")
            pass

clear()

n_players = validate_n_players(input("Enter number of players: "))

print(f"There are {n_players} players\n")

spy = randint(1, n_players)

#print(f"The spy is player {spy}")

try:
    with open("topics.csv", 'r') as fin:
        topics = [line.strip().title() for line in fin]
except FileNotFoundError:
    print("File not found.")

secret_topic = choice(topics)

#print(f"The topic is {secret_topic}")

input("Give device to first player\nPress Enter to start...")
clear()

current_player = 1

for _ in range(n_players):

    if current_player == spy:
        print("You are the Spy\n")
        input("Press Enter to hide...")
        clear()

    else:
        print(f"The topic is '{secret_topic}'\n")
        input("Press Enter when done...")
        clear()

    if current_player < n_players:
        input("Give the device to the next player\n\nPress Enter to reveal topic...")
        clear()

    current_player += 1

input("Press Enter to quit...")
