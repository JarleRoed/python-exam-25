#Word guessing game:

#reading file into list
with open('./data/ListWordGame', 'r') as impFile:
    impLines = impFile.readlines()

for i, word in enumerate(impLines, 1):
    print("word", iWord, word)

#main

numGuess = 0
#program interface
while True:
    print("--------------------------------------")
    print("-      Welcome to the word game      -")
    print("--------------------------------------")


    while numGuess > 0:
        guess = input(f"Guess word nr {iWord}. You have {numGuess} guesses.")
        if guess == '':
            print("Please give a valid input")
        elif guess == word:
            print("You guessed the word!")
            break
        else:
            print("You guessed wrong. Please try again.")
            numGuess -= 1
            if numGuess == 0:
                print("You ran out of guesses for this word.")
                print(f"The word was {word}.")

#matching iGuess
