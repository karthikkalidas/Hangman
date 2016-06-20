from __future__ import print_function
import sys
import subprocess
from random import randint


#Reading words from file and storing into a list
with open("Words.txt", 'r') as WordsListFile:
    WordsList = [line.rstrip('\n') for line in WordsListFile]

#Taking no. of words
ListLength=len(WordsList)
#Getting a random word from list
TheWord=WordsList[randint(0,ListLength-1)].upper()
TheWordLength=len(TheWord)

CurWord =['_']*TheWordLength
Used=[]
HangList=list('|HANGMAN')
HangIndex=0


while True:

	if ''.join(CurWord)==TheWord:
		print("\n\nWON")
		break

	Letter=input('Guess A Letter: ').upper()

	for i in range(0,(TheWordLength)):
		
		if (Letter==TheWord[i]):	
			LetterIndex=i
			CurWord.pop(LetterIndex)
			CurWord.insert(LetterIndex,Letter)
				

		elif(Letter not in TheWord):
			if HangIndex>=6:
				print("\n\nHANGED")
				quit()
			Used.append(Letter)
			HangList.pop(HangIndex)
			HangIndex+=1
			HangList.insert(HangIndex,'|')
			break

		i+=1


	print('Word: ',end="")
	print(*CurWord, sep='')
	print('Used: ',end="")
	print(*Used, sep='')
	print(*HangList, sep='')
	print('\n\n')




