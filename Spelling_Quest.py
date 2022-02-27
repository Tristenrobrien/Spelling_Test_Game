'''
Lucy's Spelling Game

'''

import random
import time
import webbrowser
import sys
import os

         
wordList = ['about', "wouldn't", 'almost', 'laugh', 'especially', 'crown', 'however', 'powerful', 'allowed', 'fountain', 'thousand', 'around', 'ground']
completedWords = []

youGo = ['Great Job!', 'You go girl!', 'Keep it up!', 'You are almost there!', 'Fantastic', 'You are so smart!', 'Way to go!']
youGoRand = random.choice(youGo)

print ("\nWelcome to the Spelling Quest Game!")

time.sleep(.5)
print (input('\nPress the Enter key to start: '))

print ('Here is how you play - you will be shown the first and last letter of your word.')
#os.system("say 'Here is how you play - you will be shown the first and last letter of your word.'")

print ('\nYou must spell all the words correctly to win the game!!!\n')
#os.system("say 'You must spell all the words correctly to unlock win the game!'")

time.sleep(.5)
print(input('\nPress the Enter key for your first question: '))
time.sleep(1)

def game():
    if len(wordList) != 0:  

        word = random.choice(wordList)
        dash = (len(word) - 2)
        question = (word[0:1] + ('_' * dash) + word[-1:])
        os.system("say 'Spell'" + str(word))
        print ('\nSpell the rest of this word: ' + question)
        answer = input('')
        if answer == word:
            print (youGoRand)
            completedWords.append(word)
            wordList.remove(word)
            print ('\nOnly ' + str(len(wordList)) + ' more words to go!')
            time.sleep(1.5)
            game()

        
        else:
            print ('Try again')
            time.sleep(.5)
            print ('\nSpell the rest of this word: ' + question)
            answer = input('')
            if answer == word:
                print (youGoRand)
                completedWords.append(word)
                wordList.remove(word)
                print ('\nOnly ' + str(len(wordList)) + ' more words to go!')
                time.sleep(1.5)
                game()
                
            else:
                if answer != word:
                    dash = (len(word) - 3)
                    print ('Here is a hint: ')
                    time.sleep(1)
                    question = (word[0:2] + ('_' * dash) + word[-1:])
                    print ('\nSpell the rest of this word: ' + question)
                    answer = input('')
                    if answer == word:
                        print (youGoRand)
                        completedWords.append(word)
                        wordList.remove(word)
                        print ('\nOnly ' + str(len(wordList)) + ' more words to go!')
                        time.sleep(1.5)
                        game()
                    else:
                        print ('\nWe will come back to the word.. Try a new one')
                        time.sleep(1)
                        game()
                    
                    
            
    else:
        print ('You have won the Game!')
        time.sleep(1)
        print ('''
                                   .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
       *
        *
''')
        
game()
 
