import requests
from bs4 import BeautifulSoup
import random

praise = ['Bravo', 'Great', 'Congratulations', 'Well Done', 'Hurrah', 'Kudos']

def getNewWord():
   newWord = itsMeaning = ''

   src = requests.get('https://randomword.com/').text
   soup = BeautifulSoup(src, features='html.parser')

   for i in soup.findAll('div', {'id':'random_word'}):
       newWord = i.string

   for i in soup.findAll('div', {'id':'random_word_definition'}):
       itsMeaning = i.string

   return newWord, itsMeaning

ch = input('Hey there! Wanna Play a game of Hangman?(Y/N)\n')
score = streak = 0
while ch == 'Y':
   print('\nCool!Here\'s the word:')
   word, clue = getNewWord()
   print('_ ' * len(word))
   print('\nMeaning:', clue)
   attempts = int(round(0.7 * len(word))) if int(round(0.7 * len(word))) > 7 else 7
   print('Remaining attempts:', attempts)
   print()
   guessed = '_' * len(word)
   done = ''
   while True:
       c = input('\nYour Guess: ')
       if c in done:
           print('\nYou\'ve already guessed this letter:')
           continue
       if c in word:
           for i in range(len(word)):
               if word[i] == c:
                   guessed = guessed[:i] + c + guessed[i + 1:]
               print(guessed[i], end=' ')
           print('\nRemaining attempts:', attempts)
       else:
           print('\nMeh! Try Harder')
           attempts -= 1
           print('Remaining attempts:', attempts)
       if guessed == word:
           score += attempts
           streak += 1
           print(random.choice(praise), '!\nYour score is:', score)
           print('Streak:', streak)
           ch = input('\nNice Going! Try Maintaining the streak with another word! Care to try?(Y/N)')
           break
       elif attempts == 0:
           print('\nSorry! you\'ve run out of guesses!')
           print('The Word was:', word)
           print('Your total Score is:', score)
           ch = input('\nWanna try another Word?\n')
           score = 0
           break
       done += c
       print('letters guessed: ')
       for i in done:
           print(i, end=' ')
       print()
else:
   print('Well Okay! See you next time!')
