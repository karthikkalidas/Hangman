from __future__ import print_function
import sys
import os
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

#Using lists and other such variables for creating the interface
CurWord =['_']*TheWordLength
Used=[]
HangList=list('|HANGMAN')
HangIndex=0
Letter=""

#Print function for the interface
def interface():
    text = "\rWord: {}\nUsed: {}\n{}\n".format(''.join(CurWord),''.join(Used),''.join(HangList))
    os.system('clear')
    sys.stdout.write(text)

#Final check for the word match
def finalfn():
    if ''.join(CurWord)==TheWord:
        print("\n\nWON")
        quit()

#Checks the letter and changes the lists
def letterfn():
    global HangIndex
    for i in range(0,(TheWordLength)):

        if (Letter==TheWord[i]):    
            LetterIndex=i
            CurWord.pop(LetterIndex)
            CurWord.insert(LetterIndex,Letter)
 

        elif(Letter not in TheWord):
            if HangIndex>=6:
                print("\n\nHANGED")
                print("\nThe Word is : "+TheWord+'\n\n')
                quit()
            Used.append(Letter)
            HangList.pop(HangIndex)
            HangIndex+=1
            HangList.insert(HangIndex,'|')
            break

        i+=1

while True:    
    interface()
    finalfn()
    Letter=input("Please guess the next letter: ").upper()
    letterfn()


    

    



    







