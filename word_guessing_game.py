# this is a word guessing game that will give the user the opportunity to guess characters within the word or the entire
# word itself the user will only be allows 12 chances to make the correct guess.

import random

user_name = input("Hello, what is your name: ")

print("We are going to play a game of guess that word (all associated with programming). You will be given 12 chances\n"
      "to guess either characters within our selected word or the entire word itself. Below is also the number of\n"
      "characters within the word. Good Luck,", user_name + "!")

words = ["algorithm", "debugging", "functions", "recursion", "variables",
         "databases", "framework", "bytecode", "classpath", "encapsulate",
         "iteration", "middleware", "namespace", "polymorph", "scripting"]

turns = 12

random_word = random.choice(words)
#print(random_word) #this is a check
guess_status = ["_"]*len(random_word)
count = 0

while turns > 0:
    count += 1
    print(" ".join(guess_status))
    guess = input("Please input your first character guess (a character or the entire word): ").lower()

    if len(guess) == 1:
        if guess in random_word:
            for i, char in enumerate(random_word):
                if char == guess:
                    guess_status[i] = guess

        else:
            print("Sorry the value you have selected is not within the given word.")
            turns -=1

    elif guess == random_word:
        print("Congratulations, you have guessed your word correctly, your word was", random_word + ".")
        print("It took you", count, "guesses.")
        break

    else:
        print("Sorry that is an incorrect guess.")
        turns -= 1

    if "_" not in guess_status:
        print("Congratulations, you have guessed your word correctly, your word was", random_word + ".")
        print("It took you", count, "guesses.")
        break

    if turns == 0:
        print("Game over the word was:", random_word)
        break
