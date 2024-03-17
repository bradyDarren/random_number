# the following project is meant to simulate a game of black jack.
import random

card_deck = {
    "hearts": {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
        "K": 10, "Q": 10, "A": [1, 11]
    },
    "diamonds": {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
        "K": 10, "Q": 10, "A": [1, 11]
    },
    "clubs": {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
        "K": 10, "Q": 10, "A": [1, 11]
    },
    "spades": {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
        "K": 10, "Q": 10, "A": [1, 11]
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
        return 11 if current_score + 11 <= 21 else 1


house_score = 0
user_score = 0
top_score = 21
card_count = 0
hit_me = ""

print("\nWe are going to play a game of black jack. The rules are all numerical cards are worth face value\n"
      "Jacks, Kings, and Queens are worth 10 points and Aces are worth either 1 or 11 your choice.\n"
      "If at any time your cards exceed a sum of 21 you lose (bust).\n")

print("Press the S button to start the game or the Q button to quit. ")
user_input = input(">").lower()

# try:
if user_input == "s":
    while hit_me != "p":
        user_hand = hit(card_deck)
        card_count += 1

        if user_hand["rank"] == "A":
            adjusted_ace_value = ace_value(user_hand, user_score)
            user_score += adjusted_ace_value
            print("The value of your Ace card has been automatically adjusted based on the current value of your hand,"
                  "it has been adjusted to:", adjusted_ace_value)
            print("\nUser card #", card_count, ":", user_hand["rank"], "of", user_hand["suit"], "value:",
                  adjusted_ace_value,
                  "\n Total hand value of", user_score)
            if user_score <= top_score:
                print("\nWould you like to hit(H, add another card) or pass(P, allow the computers turn to begin)?")
                hit_me = input(">").lower()
            else:
                print("BUST, HOUSE WINS")
                break

        else:
            user_score += user_hand["value"]
            print("User card #", card_count, ":", user_hand["rank"], "of", user_hand["suit"], "value:",
                  user_hand["value"],
                  "\n Total hand value of:", user_score)
            if user_score <= top_score:
                print("\nWould you like to hit(H, add another card) or pass(P, allow the computers turn to begin)?")
                hit_me = input(">").lower()
            else:
                print("BUSTED, HOUSE WINS")
                break

while house_score <= user_score <= top_score:
    house_hand = hit(card_deck)
    card_count = 0
    card_count += 1

    if house_hand["rank"] == "A":
        adjusted_ace_value = ace_value(house_hand, house_score)
        house_score += adjusted_ace_value
        print("The value of your Ace card has been automatically adjusted based on the current value of your hand,"
              "it has been adjusted to:", adjusted_ace_value)
        print("\nHouse card #", card_count, ":", house_hand["rank"], "of", house_hand["suit"], "value:",
              adjusted_ace_value,
              "\n Total hand value of", house_score)
        if house_score > top_score:
            print("BUST, USER WINS")
            break

    else:
        house_score += house_hand["value"]
        print("House card #", card_count, ":", house_hand["rank"], "of", house_hand["suit"], "value:", house_hand["value"],
              "\n Total hand value of:", house_score)
        if house_score > top_score:
            print("BUST, USER WINS")
            break

if user_score < house_score < top_score:
    print()
    print("HOUSE WINS!!!")

elif house_score < user_score < top_score:
    print()
    print("CHALLENGER WINS")
