# assignment: programming assignment 1
# author: Kevin Chen
# date: October 4th, 2022
# file: hangman.py is a program that asks the player to choose a word size between 3-12 characters and will be given a random word in the English dictionary. The player has a certain number of lives(1-10) to guess one letter at a time to complete the word, depending on the number of lives chosen.
# input: the player will input the size of the word they wish to guess along with the number of lives. They will also be required to input single letters at a time to guess the word.
# output: the program will output the letters that have been chosen so far, along with the number of lives remaining, and also the progress of the word the player is guessing with blanks indicating letters that haven't been guessed and the spots with letters indicating correct letters of the word in their proper position.
from random import choice
import random
dictionary_file = "dictionary.txt"
def print_dictionary (dictionary) :
    max_size = 12
    pass 
def get_game_options ():
  try:
    size = input('Please choose a size of a word to be guessed [3 – 12, default any size]:')
    if int(size) not in range(3,13):
      raise ValueError()
    print(f'The word size is set to {str(size)}.')
  except ValueError:
    print('A dictionary word of any size will be chosen.')
    size = random.randint(3,12)
  try:
    lives = input('Please choose a number of lives [1 – 10, default 5]:')
    if int(lives) not in range(1,11):
      raise ValueError()
    phrase = 'You have {} lives.'
    print(phrase.format(str(lives)))
  except ValueError:
    lives = 5
    phrase = 'You have {} lives.'
    print(phrase.format(str(lives)))
  return int(size), int(lives)
def import_dictionary(filename):
  dictionary = {}
  max_size = 12
  file = open(filename, 'r')
  lines = file.readlines()
  for i in range(3,12):
    words_12 = []
    words = []
    for word in lines:
      word = word.strip()
      if len(word) == i:
        words.append(word)
      elif len(word) >= max_size:
        words_12.append(word)
    dictionary[i] = words
  dictionary[12] = list(set(words_12))
  return dictionary


dictionary = import_dictionary(dictionary_file)
select = 'Y'
print('Welcome to the Hangman Game!')
while select.upper() == 'Y':
    size, lives = get_game_options()
    list_size = dictionary[size]
    game_word = choice(list_size)
    lost = 0
    used_letters = []
    game_letters = []
    for i in range(size):
        game_letters.append('__')
    while ('__' in game_letters):
        print('Letters chosen:', end = ' ')
        for letter in used_letters:
          print(letter, end = ', ')
        print()
        for blank in game_letters:
            print(blank, end = ' ')
#print('__ '*size, end = ' ')
        lives_lost = 'X' * lost
        lives_left = 'O' * lives
        print(f'lives: {lives} {lives_lost}{lives_left}')
        try:
            new_letter = input('Please choose a new letter >')
            if new_letter.upper() in used_letters:
                raise ValueError()
        except ValueError:
            while new_letter.upper() in used_letters:
                new_letter = input('Please choose a new letter >')
        used_letters.append(new_letter.upper())
#if new_letter.lower() in game_word:
        indices = []
        if new_letter.lower() in game_word:
            print('You guessed right!')
            for letter in game_word:
              if letter == new_letter.lower():
                  position = game_word.find(new_letter.lower())
                  indices.append(position)
        elif new_letter.lower() not in game_word:
            print('You guessed wrong, you lost one life.')
            lost += 1
            lives -= 1
        for i in indices:
            game_letters[i] = new_letter.upper()
        if lives == 0:
            print('Letters chosen:', end = ' ')
            print()
            [print(i, end = ', ') for i in used_letters]
            print()
            [print(i, end = ' ') for i in game_letters]
            lives_lost = 'X' * lost
            lives_left = 'O' * lives
            print(f'lives: {lives} {lives_lost}{lives_left}')
            print('You lost!  The word is', game_word.upper())
            break
        if ('__' not in game_letters):
          print('Letters chosen:', end = ' ')
          print()
          [print(i, end = ', ') for i in used_letters]
          print()
          [print(i, end = ' ') for i in game_letters]
          lives_lost = 'X' * lost
          lives_left = 'O' * lives
          print(f'lives: {lives} {lives_lost}{lives_left}')
          print('Congratulations!!!  You won!  The word is', game_word.upper())
          break
    try:
        select = input('Would you like to play again [Y/N]?')
        if select.upper() not in ['Y','N']:
            raise ValueError()
    except ValueError:
        while select.upper() not in ['Y','N']:
            select = input('Would you like to play again [Y/N]?')

print('Goodbye!')




