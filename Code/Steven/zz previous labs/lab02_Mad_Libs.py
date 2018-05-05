fruit = input('Enter a fruit: ')

nouns = input('Enter two nouns, separated by spaces: ')
nouns = nouns.split(' ')

plural_nouns = input('Enter two plural nouns, separated by spaces: ')
plural_nouns = plural_nouns.split(' ')

silly_word = input('Enter a silly word: ')

print(f'After the release of his famous trilogy, Lord of the {plural_nouns[0]}, J.R.R. Tolkien has been thrust into the {fruit}-light yet again.\nThe three books, {nouns[0]} of the Rings, The Two {plural_nouns[1]}, and Return of the {nouns[1]}, are to be followed by another book \'The {silly_word}\', which is sure to be filmed later on.')

