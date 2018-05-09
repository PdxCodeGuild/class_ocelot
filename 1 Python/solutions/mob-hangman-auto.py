import random
#load english.txt itterate through char by char
#build giant list of characters, and count letters
#CREATE DICt keys = letters values = count
#convert to giant list(most frequent letters first)

def get_word_frequecies():
    with open('../data/english.txt', 'r', encoding='utf-8') as f:
        contents = f.read().lower()
    d = {}
    for char in contents:
        if not char.isspace():
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
    d = list(d.items())
    d.sort(key=lambda t: t[1], reverse=True)


    d = [t[0] for t in d]
    return d


ordered_letters = get_word_frequecies()
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
    words = [word for word in contents if len(word) > 12]

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




wins = 0
winning_words = []
losing_words = []


for i in range(10000):
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
    for ordered_letter in ordered_letters:
        print(' '.join(guessed))
        letter = ordered_letter.upper()
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
            losing_words.append(''.join(word))
            break
        if check_win(guessed):
            print('You win!')
            winning_words.append(''.join(word))
            wins += 1
            break

    print(' '.join(guessed))



print(f'{round(wins/10000*100,2)}%')
print(f'winning words: {",".join(winning_words)}')
print(f'losing words: {",".join(losing_words)}')