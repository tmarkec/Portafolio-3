import random
import string
import os
import pyfiglet
from pyfiglet import Figlet
from hangman import hangman_as


def welcome():
    """
    Function to welcome screen which will provide user
    with rules and input field for his name.
    """
    ascii_banner = pyfiglet.figlet_format("Welcome   to   HANGMAN!!!")
    print(ascii_banner)
    print("\n")
    print("You play the game by guessing letters")
    print("that makes hidden word. With each wrong")
    print("guess you are one step closer to beeing")
    print("hanged! You can choose between 3 levels")
    print("but for start lets get your name first....")
    print("\n")

    while True:
        name = input("Please enter your name:\n").capitalize()

        if not name.isalpha():
            print("Name must be alphabets only!!!\n")
            
        else:
            clear()
            levels()
            break
    return name


def clear():
    """
    Function to clear screen through the code.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_word(word_list):
    """
    Function to get random words
    """

    words = random.choice(word_list)
    return words.upper()


def levels():
    """
    This function will ask player to choose dificult level for the game.
    """
    clear()
    print('Hello lets pick level for you!!!')
    choose = False
    lives = 0
    while choose is False:
        difficulty = input('Enter E for easy, M for medium or H for hard\n')\
            .upper()
        if difficulty == 'E':
            choose = True
            lives = 6
            return lives
        elif difficulty == 'M':
            choose = True
            lives = 4
            return lives
        elif difficulty == 'H':
            choose = True
            lives = 2
            return lives
        else:
            print('Please type E, M or H to choose dificulty levels!!!')
            choose = False
    

def game(word_list, name, lives):
    word = get_word(word_list)
    hidden_word = set(word)
    letter_alphab = set(string.ascii_uppercase)
    used_letters = set()
    tries = lives
    
    while len(hidden_word) > 0 and tries > 0:
        print(f'You have left{tries} lives')
        print('You used:', ' '.join(used_letters))
        letter_words = [letter if letter in used_letters else '-' for letter in word]
        print(hangman_as[tries])
        print('Current word is:', ' '.join(letter_words))
        

welcome()
