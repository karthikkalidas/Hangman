import sys
from random import randint

#Reading words from file and storing into a list
with open("Words.txt", 'r') as WordsListFile:
    WordsList = [line.rstrip('\n') for line in WordsListFile]

#Taking no. of words
ListLength=len(WordsList)
#Getting a random word from list
TheWord=WordsList[randint(0,ListLength-1)]
TheWordLength=len(TheWord)
print(TheWord)

for i in range(0,TheWordLength):
	print('_',end=" ")


