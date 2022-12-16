# Snake Water Gun Game :

import random
list = ["S", "W", "G"]

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print("\t \t \t*** Snake, Water, Gun Game***\n \n")
print("S for Snake, W for Water,G for Gun")

while no_of_chance < chance:
    human_choosed = input('Snake,Water,Gun : ')
    computer_choice = random.choice(list)

    if human_choosed == computer_choice:
        print("Tie Both 0 Point to each etc........")

    elif human_choosed == 'S' and computer_choice == 'G':
        computer_point = computer_point + 1
        print(f"Your Guess {human_choosed} and computer guess is {computer_choice}\n")
        print("Computer Wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")
    elif human_choosed == 'S' and computer_choice == 'W':
        human_point = human_point + 1
        print(f"Your Guess {human_choosed} and computer guess is {computer_choice}\n")
        print("Human Wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")
    elif human_choosed == 'W' and computer_choice == 'G':
        human_point = human_point + 1
        print(f"Your Guess {human_choosed} and computer guess is {computer_choice}\n")
        print("Human Wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")
    elif human_choosed == 'W' and computer_choice == 'S':
        computer_point = computer_point + 1
        print(f"Your Guess {human_choosed} and computer guess is {computer_choice}\n")
        print("computer Wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")
    elif human_choosed == 'G' and computer_choice == 'S':
        computer_point = computer_point + 1
        print(f"Your Guess {human_choosed} and computer guess is {computer_choice}\n")
        print("Human Wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")
    elif human_choosed == 'G' and computer_choice == 'W':
        human_point = human_point + 1
        print(f"Your Guess {human_choosed} and computer guess is {computer_choice}\n")
        print("Human Wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")
    else:
        print("Plz Enter Valid Input")
    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game Over")

if computer_point > human_point:
    print("....Computer Wins And You Lose....")

if computer_point < human_point:
    print("....You Wins And Computer Lose....")

print(f"Your point is {human_point} and comnputer point is {computer_point}")
