
import random

def rps():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice_rock()
    elif computer_choice == 2:
        computer_choice_paper()
    else:
        computer_choice_scissors()

def computer_choice_rock():
    user_choice = input('1 for Rock, 2 for Paper, 3 for scissors: ')
    if user_choice == "1":
        print("You tie, You chose Rock and the computer chose Rock.")
        try_again()

    if user_choice == "2":
        print("You WIN you chose Paper and the computer chose Rock")
        try_again()

    if user_choice == "3":
        print("You lose! You chose Scissors and the computer chose Rock")
        try_again()
    else:
        print( "try again")
        computer_choice_rock()

def computer_choice_paper():
    user_choice = input('1 for Rock, 2 for Paper, 3 for scissors: ')
    if user_choice == "1":
        print("You lose, You chose Rock and the computer chose Paper.")
        try_again()

    if user_choice == "2":
        print("You Tie, You chose paper and the computer chose Paper")
        try_again()

    if user_choice =="3":
        print("You win! You chose Scissors and the computer chose Paper")
        try_again()
    else:
        print("try again")
        computer_choice_paper()

def computer_choice_scissors():
    user_choice = input('1 for Rock, 2 for Paper, 3 for scissors: ')
    if user_choice == "1":
        print("You lose, You chose Rock and the computer chose Scissors.")
        try_again()

    if user_choice == "2":
        print("You tie you chose Paper and the computer chose   Scissors")
        try_again()

    if user_choice =="3":
        print("You win! You chose Scissors and the computer chose Scissors")
        try_again()
    else:
        print("try again")
        computer_choice_scissors()

def try_again():
    choice = input("Would you like to play again? y/n ")
    if choice == "y" or choice == "yes":
        rps()
    elif choice == "n" or choice == "no" or choice == "N":
        print("Thanks for playing")
        quit()
    else:
        print("Try again")
        try_again()

rps()

