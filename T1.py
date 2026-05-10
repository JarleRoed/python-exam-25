#Word guessing game:

#reading file into list
with open('./data/ListWordGame', 'r') as impFile:
    impLines = [line.strip() for line in impFile]


#program interface
    print("--------------------------------------")
    print("-      Welcome to the word game      -")
    print("--------------------------------------")

#need to change from correct word to correct letter.
for iWord, word in enumerate(impLines, 1):
    # guesses per letter:
    numGuess = len(word)
    lettGuess = []

    while numGuess > 0:

        wordDisplay = ""
        for letter in word:
            if letter in lettGuess:
                wordDisplay += letter + " "
            else:
                wordDisplay += "_ "
        print(f"\nCurrent word is {iWord}: {wordDisplay}\n")
        print(f"You have {numGuess} guesses left")

        guess = input("Guess a letter: ")

        if guess == '':
            print("Please give a valid input")
        elif len(guess) > 1:
            print("One letter at a time")
        elif guess.lower in lettGuess:
            print("You already guessed this letter")
        elif guess.lower() in word.lower():
            print("Correct letter!")
            lettGuess.append(guess.lower())
            if all(letter.lower() in lettGuess for letter in word):
                print(f"You guessed the word: {iWord}")
                break

        else:
            print("Wrong letter")
            numGuess -= 1
            if numGuess == 0:
                print(f"You ran out of guesses. The word was {word}")
print("You won the game!")
