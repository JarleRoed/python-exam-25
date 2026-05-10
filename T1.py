#Word guessing game:



#reading file into list
with open('./data/ListWordGame', 'r') as impFile:
    impLines = impFile.readlines()

for i, word in enumerate(impLines, 1):
    print("word", iWord, word)

#main
#program interface

#matching iGuess