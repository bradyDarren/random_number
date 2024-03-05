# This program is used to create a game called pig where the objective is to reach a score of 100.
# through the sum of the rolls you have made. You can either select to stop rolling and safely take
# your points or continue to roll in effort to obtain the score of 100 or higher to win the game.
# If you happen to roll a 1 the all the point that you have previously scored will now be 0.

import random

score_limit = 50

one_score = 0
two_score = 0

current_turn = 1

player_one = input("Hello, Please input your name Player 1: ").lower()
player_two = input("Hello, Please input your name Player 2: ").lower()


while one_score < score_limit and two_score < score_limit:
    random_roll = random.randint(1, 6)
    print("Current score: Player one:", one_score, "Player two:", two_score)
    if current_turn % 2 == 1:
        print()
        one_roll = input("Roll Player One (to roll press key r) or Pass (to pass press key p): ").lower()

        if one_roll == "r":
            print()
            print("You rolled a: ", random_roll)
            one_score += random_roll
            if random_roll == 1:
                print()
                print("Back to 0 you go")
                current_turn += 1
                one_score = 0

        elif one_roll == "p":
            current_turn += 1
            print()
            print("You have passed.")

        else:
            current_turn += 1
            print()
            print("Make a valid selection, you have lost your turn.")

    else:
        print()
        two_roll = input("Roll Player Two (to roll press key r) or Pass (to pass press key p): ").lower()

        if two_roll == "r":
            print()
            print("You rolled a: ", random_roll)
            two_score += random_roll
            if random_roll == 1:
                print()
                print("Back to 0 you go")
                current_turn += 1
                two_score = 0

        elif two_roll == "p":
            current_turn += 1
            print()
            print("You have passed.")

        else:
            current_turn += 1
            print("Make a valid selection, you have lost your turn.")

    if one_score >= score_limit or two_score >= score_limit:
        break

if one_score >= score_limit:
    print()
    print("Player one is Victorious!!!!")

elif two_score >= 100:
    print()
    print("Player two is Victorious!!!!")




