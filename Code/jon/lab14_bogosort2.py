import random

i=0
valid = False
while not(valid):
    word = input("Enter word to be mixed > ")
    if len(word) <= 1:
        ("not valid!")
    else:
        valid = True

wordlist = list(word)

resorted = False
while not (resorted):
    random.shuffle(wordlist)
    i += 1
    print ("attempts", i)
    print (wordlist)
    if list(word) == wordlist:
        print ("Sorted!")
        break