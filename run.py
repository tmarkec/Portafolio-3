import random
import string
import os
import pyfiglet
# import colorama
from hangman import hangman_as
from words import word_list
# from colorama import Fore, init
# init(autoreset=True)


def welcome():
    """
    Function to welcome screen which will provide user
    with rules and input field for his name.
    """
    welcome_text = pyfiglet.figlet_format('Welcome to Hangman')
    print(welcome_text)
    print("\n")
    print("Rules of this game are fairly simple, you are")
    print("guessing letters one by one that makes the hidden word.")
    print("With each wrong guess you are one step closer to beeing")
    print("hanged! You can choose different levels of difficulty!")
    print("But let's not skip the steps now, first enter your name!")
    print("\n")
    global name

    while True:
        name = input("Please enter your name:\n").strip().capitalize()

        if not name.isalpha():
            print( "Name must be alphabets only!!!\n")
            
        else:
            clear()
            break
    return name


def clear():
    """
    Function to clear terminal through the game.
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
    This function will ask player to choose dificulty level for the game.
    """
    clear()
    print('\n')
    print(f'What a lovely name {name}, lets pick level for you!!!')
    print('\n')
    while True:
        try:
            difficulty = input('Please type E for easy, M for medium or H\
                                 for hard!\n').strip().upper()
            if difficulty == 'E':
                lives = 6
                break
            if difficulty == 'M':
                lives = 4
                break
            if difficulty == 'H':
                lives = 2
                break
            else:
                raise ValueError(f'Please {name} type E or M or H for \
                                    difficulty level!\n')
        except ValueError as e_rr:
            print(f"Invalid input:{e_rr}")

    clear()  
    return lives
    

def game():
    """
    This function will run the game, sets lives and 
    template for player to play depends on the level he choose.
    The game will finish when user either guess the word or
    loose all lives.

    """
    clear()
    word = get_word(word_list)
    hidden_word = set(word)
    letter_alphab = set(string.ascii_uppercase)
    used_letters = set()
    tries = levels()

    while len(hidden_word) > 0 and tries > 0:
        print(f'{name} you have {tries} lives left for this round')
        print('You used:', ' '.join(used_letters))
        letter_words = \
            [letter if letter in used_letters else '-' for letter in word]

        print(hangman_as[tries])
        print('Current word is:', ' '.join(letter_words))

        user_guess = input('\nTry to guess letter: \n').upper()
        clear()
        if user_guess in letter_alphab - used_letters:
            used_letters.add(user_guess)
            if user_guess in hidden_word:
                hidden_word.remove(user_guess)
            else:
                tries -= 1
                print('Your guess is not in the word, try again!')
       
        elif user_guess in used_letters:
            print( 'You used this letter already, try again')
        
        else:
            print('Unrecognized character, please try \
                                again with letter!')

    if tries == 0:
        clear()
        custom_fig = pyfiglet.figlet_format(f'Sorry {name} you lost!!!')
        print(custom_fig)
        print(f'The word we were looking for was {word}')
        print(hangman_as[tries])
        end()

    else:
        clear()
        text_win = pyfiglet.figlet_format(f'Well done {name}, you won!!!')
        print(text_win)
        end()
    

def end():
    """ 
    Function that will ask user if he wants to play again.
    """

    while True:
        again = input('Would you like to play again? \n Y/N?\n').upper()
        try:
            if again == 'Y':
                clear()
                game()
                break
            elif again == "N":
                clear()
                thank_you()
                break
            else:
                raise ValueError('\nYou must type Y or N.')
        except ValueError as e:
            print(f'Try again: {e}')


def thank_you():
    """
    This function will just print text for user 
    when he decided to stop playing game
    """
    clear()
    thank_text = pyfiglet.figlet_format(f'Thank you for playing this game {name}!')
    print(thank_text)


welcome()
game()
