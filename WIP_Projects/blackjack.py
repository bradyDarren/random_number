# the following project is meant to simulate a game of black jack.
import random

card_deck = {
    "hearts": {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
        "K": 10, "Q": 10, "A": [1, 10]
    },
    "diamonds": {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
        "K": 10, "Q": 10, "A": [1, 10]
    },
    "clubs": {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
        "K": 10, "Q": 10, "A": [1, 10]
    },
    "spades": {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
        "K": 10, "Q": 10, "A": [1, 10]
    }
}


# Step 1: retrieve a list of our card suites.
# suit = list(card_deck.keys())
# print(suit)  # For Test

# Step 2: make a randomized selection of our suit list.
# random_suit = random.choice(suit)
# print(random_suit)  # For Test

# Step 3: retrieve a list of the cards associated with our random suit.
# rank = list(card_deck[random_suit].keys())
# print(rank)  # For Test

# Step 4: make a random selection from the rank list
# random_rank = random.choice(rank)
# print(random_rank)  # For Test

# Step 5: pulls the value of the card
# card_value = card_deck[random_suit][random_rank]
# print(card_value)  # For Test

# function used to draw a card
def hit(deck):
    if not deck:
        raise ValueError("Card deck is either empty or not provided")
    rand_suit = random.choice(list(deck.keys()))
    rand_rank = random.choice(list(deck[rand_suit].keys()))
    card_value = deck[rand_suit][rand_rank]
    return {"rank": rand_rank, "suit": rand_suit, "value": card_value}


def ace_value(user_cards, current_score):
    if user_cards["rank"] == "A":
        return 11 if current_score + 11 >= 21 else 1
    else:
        return user_cards["value"]


comp_score = 0
user_score = 0
top_score = 21
card_count = 0

print("\nWe are going to play a game of black jack. The rules are all numerical cards are worth face value\n"
      "Jacks, Kings, and Queens are worth 10 points and Aces are worth either 1 or 11 your choice.\n"
      "If at any time your cards exceed a sum of 21 you lose (bust).\n")

# assesses the score of both the computer and the user
while user_score <= top_score or comp_score <= top_score:
    user_hand = hit(card_deck)  # draws a random card from our card_deck
    card_count += 1

    if user_hand["rank"] == "A":
        adjusted_ace_value = ace_value(user_hand, user_score)
        user_score += adjusted_ace_value
        print("The value of your Ace card has been automatically adjusted to:", adjusted_ace_value, "based on your"
                                                                                                    "current score")
    else:
        print("User hand Card 1:", user_hand["rank"], "of", user_hand["suit"], "value:", user_hand["value"])
        user_score = user_hand["value"]
        if card_count <= 1:
            print("Press the f key to flip your second card over:")
            user_input = input(">").lower()
            if user_input == "f":
                user_hand = hit(card_deck)
                print("User hand Card 2:", user_hand["rank"], "of", user_hand["suit"], "value:", user_hand["value"])
                user_score += user_hand["value"]
                print("Your current hand value is:", user_score)
                print("Would you like to hit(H, add another card) or pass(P, allow the computers turn to begin)?")
                hit_me = input(">").lower()
                if hit_me == "h":
                    user_hand = hit(card_deck)
                    print("User hand Card 3:", user_hand["rank"], "of", user_hand["suit"], "value:",
                          user_hand["value"])
                    user_score += user_hand["value"]
                    print("Your current hand value is:", user_score)
                    if user_score < top_score:
                        print(
                            "Would you like to hit(H, add another card) or pass(P, allow the computers turn to begin)?")
                        hit_me = input(">").lower()
                    elif user_score > top_score:
                        print("BUSTED. You lose!!!")
                        print("Below is the computers hand: ")
                        comp_hand = hit(card_deck)
                        print("Comp hand Card 1:", comp_hand["rank"], "of", comp_hand["suit"], "value:",
                              comp_hand["value"])
                        comp_score += comp_hand["value"]
                        print("Comp current hand value is:", comp_score)
                        comp_hand = hit(card_deck)
                        print("Comp hand Card 2:", comp_hand["rank"], "of", comp_hand["suit"], "value:",
                              comp_hand["value"])
                        comp_score += comp_hand["value"]
                        print("Comp current hand value is:", comp_score)

                elif hit_me == "p":
                    comp_hand = hit(card_deck)
                    if comp_hand["rank"] == "A":
                        adjusted_ace_value = ace_value(user_hand, user_score)
                        comp_score += adjusted_ace_value
                        print("Comp hand Card 1:", comp_hand["rank"], "of", comp_hand["suit"], "value:",
                              comp_hand["value"])
                    else:
                        print("Comp hand Card 1:", comp_hand["rank"], "of", comp_hand["suit"], "value:",
                              comp_hand["value"])

    if user_score > top_score or comp_score > top_score:
        break
