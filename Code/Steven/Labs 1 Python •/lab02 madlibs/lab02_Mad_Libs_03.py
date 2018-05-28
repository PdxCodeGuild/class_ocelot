import re, time

nouns_list = []
plural_nouns_list = []

# Defaults
fruit_d = 'banana'
noun1_d = 'table'
noun2_d = 'woodchipper'
plural_noun1_d = 'garbanzos'
plural_noun2_d = 'hushpuppies'
silly_word_d = 'Jackalope'

# Madlibs word inputs
fruit = input('Enter a fruit: ')                                # INPUT 1
if fruit == '':                                                 # If input is none ('enter')
    fruit = fruit_d                                             # then set default.

fruit = fruit.title()                                           # Capitalize
print(fruit,'\n')                                               # Print


nouns = input('Enter two nouns, separated by spaces: ')         # INPUT 2 & 3
regex_string = r"^(\w+ \w+)"                                    # Define regex matching 'word word'
if re.search ( regex_string , nouns ) == True:                  # If input is in that form
# TODO What is best way to make this a list?
    print(type(nouns))
    print(nouns, nouns.split ( ' ' ))

    nouns = nouns.split ( ' ' )                                 ## split to 2 separate words.

else:
    print(type(nouns))
    nouns = noun1_d + ' ' + noun2_d                             # then set word1 & word2 default...


nouns = nouns.title()                                           # Capitalize
print(f'{nouns}\n')                                             # Print

plural_nouns = input('Enter two plural nouns, separated by spaces: ')   # INPUT 4 & 5
regex_string = r"^(\w+ \w+)"                                    # Define regex matching 'word word'
if re.search ( regex_string , plural_nouns ) == True:           # If input is in that form
    plural_nouns = plural_nouns.split ( ' ' )                   ## split to 2 separate words.
# TODO What is best way to make this a list?
else:
    plural_nouns = plural_noun1_d + ' ' + plural_noun2_d            # then set word1 & word2 default...


plural_nouns = plural_nouns.title()                             # Capitalize
print(f'{plural_nouns}\n')                                      # Print

silly_word = input('Enter a silly word: ')                      # INPUT 6
if silly_word == '':                                            # If input is none ('enter')
    silly_word = silly_word_d                                   # then set default.
silly_word = silly_word.title()                                 # Capitalize
print(f'{silly_word}\n')                                        # Print

time.sleep(2)

# Delay effect

print('Now creating Mad lib...')

time.sleep(3)

print('Almost done...')

time.sleep(3)

print('Cranking the humor up to eleven...')

time.sleep(4)

print('MAD LIB COMPLETE: \n\n')

# Print the Madlibs output string.
print(f'After the release of his famous trilogy, Lord of the {plural_nouns[0]}, J.R.R. Tolkien has been thrust into the {fruit}-light yet again. \n\nThe three books, {nouns[0]} of the Rings, The Two {plural_nouns[1]}, and Return of the {nouns[1]} , are to be followed by another book The {silly_word}, which is sure to be filmed later on.')

