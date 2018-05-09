import random

hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\. |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\. |
./ \  |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\. |
./ \. |
      |
=========''']

hangman_pics.reverse()


# def myfunc(a, b):
#     print(a)
#     print(b)
#
# a = 5
# b = 6
# x = 1
# y = 2
# myfunc(x, y)


# functions ---------------------------

# return true if there are any underscores, false otherwise
# def check_underscores(letters):

def check_win(guessed):
    return '_' not in guessed


# def load_words(): return a list of words
def load_words():
    with open('../data/english.txt', 'r', encoding='utf-8') as f:
        contents = f.read().upper().split('\n')
    words = [word for word in contents if len(word) > 8]

    return words


# take two lists - one of underscores and one of letters, and a letter#
# find the letter in the list of letters for the word
# replace the element in the underscore list with the same letter
# if we don't find it, increment the number of mistakes, display the hangman

# ['a', 'a', 'r', 'd']
# ['_', '_', '_', ...]


def check_letter(word, guessed, letter):
    r = False
    for i in range(len(word)):
        if word[i] == letter:
            guessed[i] = letter
            r = True
    return r


# try to replace the underscores with the matching letters#
# if it does replace something, return true, otherwise return false
# steps to take ------------------------------------------------------
# open english.txt, have a minimum length of the word #
# put all the words into a list#
# randomly pick a word out of that list#
words = load_words()

word = random.choice(words)

# make the word into a list#

word = list(word)

# make a list of of underscores, same length as the word#

guessed = ['_'] * len(word)

# start a counter at 0

death_counter = len(hangman_pics)

guessed_letters = []

# ask for a letter, store in a variable#

# Read Evaluate Print Loop
while True:
    print(' '.join(guessed))
    letter = input('Guess a letter: \n>').upper()
    # check to see if the letter has been guessed before
    # if it has, we don't try it, tell the user, express snarkiness

    if list(letter) == word:
        print('awesome, you win.')
        break
    elif len(letter) > 1:
        print("One letter at a time please. b")
        continue
    if letter in guessed_letters:
        print('letter already guessed, guess again. c\'mon man #snark')
        continue
    guessed_letters.append(letter)
    # if there aren't any underscores in the underscore list
    if not check_letter(word, guessed, letter):
        death_counter -= 1
        print(f'Letter not found. {death_counter} tries remaining.')
        print(hangman_pics[death_counter])

    print(f"Guessed letters: {', '.join(guessed_letters)}")

    # if the mistake counter is 0, you lose
    if death_counter == 0:
        print('loser')
        print(''.join(word))
        break
    if check_win(guessed):
        print('You win!')
        break



