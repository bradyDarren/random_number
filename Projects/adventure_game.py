# this is the creation of an adventure game similar to sims/pick your own story
# within the program we will allow you to make a series of choices resulting in various
# outcomes depending on the combinations of choices you have made.

user_name = input("Hello, welcome to the adventure game what should we call you?: ")
print(user_name, "adventure is out there, and we are going to explore it.")

answer = input("You are on a dirt road and the road comes to an end "
               "you have a\nchoice of going left or right?: ").lower()

# if you choose the left path
#    while True:
if answer == "left":
    answer = input("You cross paths with a stranger and he offers you a choice\n"
            "of the a boat, sword, or a warm coat.\n"
            "What will you choose (boat/sword/coat)?: ").lower()

# if you choose the boat
    if answer == "boat":
        answer = input("Not long after the stranger you come to a river, you safely cross.\n\n"
                "As you proceed on your journey you have now come to a large\n"
                "city and a merchant has asked you to exchange your boat for a camel and\n"
                "satchels of water. Will you accept this trade (yes/no)?: ").lower()

# if you decided to sell your boat
        if answer == "yes":
            print("Shortly are leaving the city you cross the desert unscaved, "
                           "make it to paradise and win the game.")

        elif answer == "no":
            print("Shortly are leaving the city you come to a dessert, you try and cross run and run out of water and lose the game.")

# if you choose the sword
    elif answer == "sword":
        answer = input("Not long after the stranger you come to a river, you can either swim across or walk the"
                " long way around. Which one would you like to do(swim/walk)?: ").lower()

# if you choose to swim across the river
        if answer == "swim":
            print("You swam across into Hippo territory and a were killed. Game over! ")

        elif answer == "walk":
            print("You walk for mile and miles run out of water and die.")

        else:
            print("Please enter a valid option.")

# if you choose the coat
    elif answer == "coat":
        answer = input( "Not long after the stranger you come to a river, you can either swim across or walk the"
                " long way around. Which one would you like to do(swim/walk)?: ").lower()

        if answer == "swim":
            print("You swam across into Hippo territory and a were killed. Game over! ")

        elif answer == "walk":
            print("You walk for mile and miles run out of water and die.")

        else:
            print("Please enter a valid option.")

# if none of the provided options are picked
    else:
        print("Please enter a valid option.")

# if you choose the right option
elif answer == "right":
    answer = input("You walk for miles and encounter thieves and they take everything you\nhave and imprison you."
            " You have lost the game!").lower()

else:
    print("Please enter a valid option.")

