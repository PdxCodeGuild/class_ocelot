import re, time

two_words = input('Enter two words, separated by a space:\n > ').title()

print(f'{two_words} is a {type(two_words)}')

two_words_list = two_words.split ( ' ' ))

print(f'{two_words_list} is a {type(two_words_list)}')

# regex_string = r"^(\w+ \w+)"                                    # Define regex matching 'word word'
#
# if re.search ( regex_string , nouns ) == True:                  # If input is in that form
#     print(nouns, nouns.split ( ' ' ))
#     nouns = nouns.split ( ' ' )                                 ## split to 2 separate words.
#     print('REGEX MATCH') # TESTER
#     print(type(nouns))
#
# else:
#     # print(type(nouns)) # TESTER
#     nouns = noun1_d + ' ' + noun2_d                             # then set word1 & word2 default...
#
# print(f'{nouns}\n')                                             # Print
#

