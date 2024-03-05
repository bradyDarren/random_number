#introduction to the game
print("Welcome to the Market game!!!")

#asking the player if they want to play
play = input('Would you like to answer some questions about the progression of the stock market'
            'from 2010 to 2020?: ')
if play.lower() != 'yes':
    print('Thank you for your honesty! Good day!')
else:
    print('I hope you are ready for a challenge!!')

score = 0

#Question #1
answer = input('What was the approximate percentage increase of the S&P 500 index from January 1, 2010, to December 31, 2020?\n'
                'A)100%\n'
                'B)190%\n'
                'C)300%\n'
                'D)400%\n')

if answer.lower() != 'b':
    print('Incorrect!')
else:
    print('Correct!')
    score +=1

#Question #2
answer = input('Which company became the first to reach a $2 trillion market cap in 2020?\n'
               'A) Amazon\n'
               'B) Apple\n'
               'C) Microsoft\n'
               'D) Google (Alphabet)\n')

if answer.lower() != 'b':
    print('Incorrect!')
else:
    print('Correct!')
    score +=1

#Question #3
answer = input('What significant event caused a major stock market crash in March 2020?\n'
               'A) Brexit vote\n'
               'B) U.S. Presidential Election\n'
               'C) COVID-19 pandemic\n'
               'D) Federal Reserve rate hike\n')

if answer.lower() != 'c':
    print('Incorrect!')
else:
    print('Correct!')
    score +=1

#Question #4
answer = input('Which sector saw the most significant growth during the 2010s?\n'
               'A) Energy\n'
               'B) Technology\n'
               'C) Healthcare\n'
               'D) Consumer Discretionary\n')

if answer.lower() != 'b':
    print('Incorrect!')
else:
    print('Correct!')
    score +=1

#Question #5
answer = input('Which of the following companies was not part of the FAANG group that significantly influenced the market\'s growth?\n'
               'A) Facebook\n'
               'B) Amazon\n'
               'C) Alphabet (Google)\n'
               'D) IBM\n')

if answer.lower() != 'd':
    print('Incorrect!')
else:
    print('Correct!')
    score +=1

#Question #6
answer = input('In what year did the Dow Jones Industrial Average first close above 20,000 points?\n'
               'A) 2015\n'
               'B) 2016\n'
               'C) 2017\n'
               'D) 2018\n')

if answer.lower() != 'c':
    print('Incorrect!')
else:
    print('Correct!')
    score +=1

#Question #7
answer = input('Which event is often credited with helping to initiate the longest bull market in history, which lasted from 2009 until early 2020?\n'
               'A) The end of the Great Recession\n'
               'B) The European sovereign debt crisis resolution\n'
               'C) The U.S. Federal Reserve\'s quantitative easing program\n'
               'D) The signing of the Paris Agreement\n')

if answer.lower() != 'c':
    print('Incorrect!')
else:
    print('Correct!')
    score +=1

#Question #8
answer = input('What was one of the major contributing factors to the stock market\'s recovery and growth after the 2008 financial crisis?\n'
        'A) Increase in oil prices\n'
        'B) Decrease in technology stock values\n'
        'C) Low-interest rates and quantitative easing\n'
        'D) High inflation rates\n')

if answer.lower() != 'c':
    print('Incorrect!')
else:
    print('Correct!')
    score +=1

#Question #9
answer = input('Which of the following indices represents the performance of small-cap stocks in the United States?\n'
        'A) S&P 500\n'
        'B) Dow Jones Industrial Average\n'
        'C) NASDAQ Composite\n'
        'D) Russell 2000\n')

if answer.lower() != 'd':
    print('Incorrect!')
else:
    print('Correct!')
    score +=1

#Question #10
answer = input('What innovative technology sector began to significantly influence the stock market during this period?\n'
        'A) Renewable energy\n'
        'B) Social media\n'
        'C) Electric vehicles\n'
        'D) All of the above\n')

if answer.lower() != 'd':
    print('Incorrect!')
else:
    print('Correct!')
    score +=1

print('You got '+str(score)+ ' out of 10 correct')
print('You scored '+str((score/10)*100)+'% out of %100')