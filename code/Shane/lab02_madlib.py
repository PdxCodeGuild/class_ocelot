import random

#You have to walk before you run.

def version1():
    noun = input("Provide a name\n")
    verb1 = input("Provide a verb\n")
    verb2 = input("Provide a verb\n")

    print(f"{noun}, you have to {verb1} before you {verb2}!")

version1()


def version2():
    noun = input("Provide as many names as you like separated by spaces\n").split(" ")
    verbs = input("Provide as many verbs as you like separated by spaces\n").split(" ")

    print(f"{random.choice(noun)}, you have to {random.choice(verbs)} before you {random.choice(verbs)}!")

version2()

def version3():
    new_story = "yes"
    while new_story == "yes":
        noun = input("Provide as many names as you like separated by spaces\n").split(" ")
        verbs = input("Provide as many verbs as you like separated by spaces\n").split(" ")
        same_story = 'yes'
        while same_story == 'yes':
            print(f'{random.choice(noun)}, you have to {random.choice(verbs)} before you {random.choice(verbs)}!')
            same_story = input("Would you like the same story again? yes or no\n").lower()
            if same_story == 'no':
                new_story = input("Would you like to make a new story? yes or no\n").lower()

version3()