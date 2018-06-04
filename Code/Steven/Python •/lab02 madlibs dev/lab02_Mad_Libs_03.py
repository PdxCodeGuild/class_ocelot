import re, time

nouns_list = []
plural_nouns_list = []

# Default values, entered if user hits 'Enter' without any data. '.title' capatalizes the word(s).
fruit_d = 'banana'.title()
noun1_d = 'table'.title()
noun2_d = 'woodchipper'.title()
plural_noun1_d = 'garbanzos'.title()
plural_noun2_d = 'hushpuppies'.title()
silly_word_d = 'jackalope'.title()

# Madlibs word inputs
fruit = input('Enter a fruit: ').title()                        # INPUT 1 (+ Capitalize)
if fruit == '':                                                 # If input is none ('enter')
    fruit = fruit_d                                             # then set default.
print(fruit,'\n')                                               # Print

nouns = input('Enter two nouns, separated by spaces: ').title() # INPUT 2 & 3 (+ Capitalize)
regex_string = r"^(\w+ \w+)"                                    # Define regex matching 'word word'

if re.search ( regex_string , nouns ) == True:                  # If input is in that form
# TODO What is best way to make this a list?
    print(nouns, nouns.split ( ' ' ))
    nouns = nouns.split ( ' ' )                                 ## split to 2 separate words.
    print('REGEX MATCH') # TESTER
    print(type(nouns))

else:
    # print(type(nouns)) # TESTER
    nouns = noun1_d + ' ' + noun2_d                             # then set word1 & word2 default...

print(f'{nouns}\n')                                             # Print

plural_nouns = input('Enter two plural nouns, separated by spaces: ').title()   # INPUT 4 & 5 (+ Capitalize)
regex_string = r"^(\w+ \w+)"                                    # Define regex matching 'word word'

if re.search ( regex_string , plural_nouns ) == True:           # If input is in that form
    print('GOOD')
    exit()
    # plural_nouns_list =
    # plural_nouns = plural_nouns_list.split ( ' ' )                   ## split to 2 separate words.
# TODO What is best way to make this a list?
else:
    plural_nouns = plural_noun1_d + ' ' + plural_noun2_d        # then set word1 & word2 default...


print(f'{plural_nouns}\n')                                      # Print

silly_word = input('Enter a silly word: ').title()              # INPUT 6 (+ Capitalize)
if silly_word == '':                                            # If input is none ('enter')
    silly_word = silly_word_d                                   # then set default.
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

