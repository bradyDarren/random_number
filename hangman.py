# this is a game of hangman that will allow us to be able to guess the word given a hint at the beginning of the game.

import random


# formula to locate and remove the underscores within the randomized word. This will keep the player from thinking they
# still need to guess a word when that word is actually a space.
def replace_space(word, placeholder, index):
    if index < 0 or index >= len(word):
        return placeholder
    return placeholder[:index] + " " + placeholder[index + 1:]


# declaration of our storage of words
word_bank = ["spongebob", "patrick", "squidward", "mr. krabs", "plankton", "sandy cheeks", "gary", "bikini bottom",
             "krusty krab", "chum bucket", "jellyfish fields", "squilliam", "mermaid man", "barnacle boy",
             "flying dutchman", "krabby patty", "kelp shake", "goo lagoon", "pineapple house", "boating school"]

# declaring our random word choice from our word_bank
selected_word = random.choice(word_bank)

attempts = len(selected_word) + 2

print(selected_word)  # Test Line

guess_status = [" " if char == " " else "_" for char in selected_word]  # creates underscores the length of the word
find_space = selected_word.find(" ")  # finds the location of our spaces within a word

while attempts > 0:

    guess_update = "".join(guess_status)
    print(replace_space(selected_word, guess_update, find_space))
    user_guess = (input("Guess the word!! HINT: word is associated with the the famous show SpongeBob SquarePants: ")
                  .lower())

    if user_guess in selected_word:
        for i, char in enumerate(selected_word):
            if char == user_guess:
                guess_status[i] = user_guess
        attempts -= 1
        print("You have", attempts, " attempts left.")

    elif user_guess not in selected_word:
        attempts -= 1
        print("Sorry the value you have selected is not within the given word.")
        print("You have", attempts, " attempts left.")

    guess_update = "".join(guess_status)

    if "_" not in guess_update:
        print("Congrats, you have won the game. Your word was: ", selected_word + ".")
        break

    if attempts == 0:
        print("Sorry Game Over you word was: ", selected_word + ".")
        break

