#Word guessing game:

#reading file into list
with open('./data/ListWordGame', 'r') as impFile:
    impLines = [line.strip() for line in impFile]


#program interface
    print("--------------------------------------")
    print("-      Welcome to the word game      -")
    print("--------------------------------------")

for iWord, word in enumerate(impLines, 1):
    # guesses per letter:
    numGuess = len(word)

    while numGuess > 0:
        guess = input(f"Guess word nr {iWord}. You have {numGuess} guesses.")

        if guess == '':
            print("Please give a valid input")
        elif guess == word:
            print("You guessed the word!")
            iWord += 1
            break
        else:
            print("You guessed wrong. Please try again.")
            numGuess -= 1
            print(f"The word is {word}")

            if numGuess == 0:
                print("You ran out of guesses for this word.")
                print(f"The word was {word}.")
                break
print("You won the game!")

