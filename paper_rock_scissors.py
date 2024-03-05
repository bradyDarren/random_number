import random

# intro to the game.
print("Let's play a game of Paper, Rock, Scissors:")

# keeping track of the amount of wins that we have
user_wins = 0
computer_wins = 0
# declaring our options
options = ["paper","rock","scissors"]

while True:
    user_input =input("Select an option Rock, Paper, Scissors, or Q to quit: ").lower()
    if user_input == "q":
        print("You have quit the game. Have a nice day!")
        break

    if user_input not in options:
        print("Please select an available option next time")
        continue
    # declaration of the parameters for our random number.
    random_number = random.randint(0, 2)

    computer_input = options[random_number]
    print("The computer choose", computer_input)

    if user_input == "rock".lower() and computer_input == "scissors".lower():
        user_wins += 1
        print("You bested the computer this round!")
        print("Current score: Computer:", computer_wins,"Challenger:",user_wins)
    elif user_input == "paper".lower() and computer_input == "rock".lower():
        user_wins += 1
        print("You bested the computer this round!")
        print("Current score: Computer:", computer_wins,"Challenger:",user_wins)
    elif user_input == "scissors".lower() and computer_input == "paper".lower():
        user_wins += 1
        print("You bested the computer this round!")
        print("Current score: Computer:", computer_wins, "Challenger:", user_wins)
    else:
        computer_wins += 1
        print("You have been defeated this round!")
        print("Current score: Computer:", computer_wins, "Challenger:", user_wins)

    if computer_wins >= 3:
        print("Robots are taking over! You have been beaten!")
        break
    elif user_wins >= 3:
        print("Humans rules over metal! You have won!")
        break

#NOTES ---------
#during this project you named your variable random which is a keyword and cannot be used.
#you made your list options capitalized and used the .upper method on the user input instead of .capitalize method.
#Learned that coding is continuous testing as you run through your code test early and test often.





