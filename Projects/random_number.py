import random

print('Lets play a game of guess the number.')

user_max = input('Choose a number (this number will be the max that your random number can be):')

if user_max.isdigit():
    user_max = int(user_max)

    if user_max <= 0:
        print("Please input a number above 0.")
        quit()
    else:
        random_num = random.randint(0,user_max)

else:
    print('Please input a number next time.')
    quit()

count = 0

while True:
    count += 1
    guess = input('What is your guess?:')

    if guess.isdigit():
        guess = int(guess)
    else:
        print('Please be sure to input a number next time.')
        continue

    if guess == random_num:
        print('You FINALLY got it correct')
        print('It took you', count, 'tries')
        break
    else:
        if guess > random_num:
            print('You got it wrong, try again.')
            print('Your guess was too high')
        else:
            print('You got it wrong try again!')
            print('Your guess was too low')