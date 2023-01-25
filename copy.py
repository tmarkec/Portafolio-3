import random
import string
import os
import pyfiglet
from colorama import Fore, init
from hangman import hangman_as
from words import word_list
init(autoreset=True)
width = os.get_terminal_size().columns


def welcome_screen():
    """
    Function to welcome screen which will provide user
    with rules and input field for his name.
    """
    welcome_text = pyfiglet.figlet_format('Hangman')
    print(welcome_text)
    global name
    while True:
        name = input("Please enter your name:\n".center(width)).strip()\
            .capitalize()
        print('\n')
        print('\n')
        if not name.isalpha():
            print(Fore.RED + "Name must be alphabets only!!!\n".center(width))
        else:
            clear()
            break
    return name


def clear():
    """
    Function to clear terminal through the game.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_word():
    """
    Function to get random words
    """

    words = random.choice(word_list)
    return words.upper()


def rules():
    """
    This function will display rules to the user
    """

    clear()
    welcome_text = pyfiglet.figlet_format('Hangman rules')
    print(welcome_text)
    print("\n")
    print("Rules of this game are fairly simple!!!".center(width))
    print("1. You are guessing letters one by one that makes"
          "hidden word.".center(width))
    print("2. With each wrong guess you are losing a life".center(width))
    print("3. How many lives you have depends on the level you chose".center(
        width))
    print("4. You win the game by guessing all the letter in word".center(
        width))
    print(Fore.LIGHTYELLOW_EX + "HARD= 3 tries, MEDIUM="
                                "5 tries,EASY=7 tries\n".center(width))
    while True:
        pas_b = input("Type B to go back.".center(width)).upper()

        if pas_b == 'B':
            game()
            break
        else:
            print('Please type letter B')


def levels():
    """
    This function will ask player to choose dificulty level for the game.
    Or he can choose to read rules of the game
    """
    clear()
    print(f'What a lovely name {name}, lets get started!!!'.center(width))
    print('\n')
    while True:
        try:
            print(Fore.GREEN + 'Please type E for easy'.center(width))
            print(Fore.CYAN + 'Please type M for medium'.center(width))
            print(Fore.MAGENTA + 'Please type H for hard'.center(width))
            print('Or type R for rules'.center(width))
            difficulty = input(''.center(width)).strip().upper()
            if difficulty == 'E':
                lives = 7
                break
            if difficulty == 'M':
                lives = 5
                break
            if difficulty == 'H':
                lives = 3
                break
            if difficulty == "R":
                rules()
                break
            else:
                clear()
                raise ValueError(
                    Fore.RED + ('Please follow simple instuctions!!!'.center(
                        width)))
        except ValueError as e_rr:
            print(f"Invalid input:{e_rr}".center(
                        width))
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
    word = get_word()
    hidden_word = set(word)
    letter_alphab = set(string.ascii_uppercase)
    used_letters = set()
    tries = levels()

    while len(hidden_word) > 0 and tries > 0:
        letter_words = \
            [letter if letter in used_letters else '-' for letter in word]
        print(hangman_as[tries])
        print(' '.join(letter_words).center(width))
        print(f'{name} you have {tries} lives left for this round')
        print('You used:', ' '.join(used_letters))

        user_guess = input('Try to guess letter:\n'.center(width)).upper()
        clear()
        if user_guess in letter_alphab - used_letters:
            used_letters.add(user_guess)
            if user_guess in hidden_word:
                hidden_word.remove(user_guess)
            else:
                tries -= 1
                print(Fore.RED + 'Your guess is not in the word,'
                                 'try again!'.center(width))
        elif user_guess in used_letters:
            print(Fore.YELLOW + 'You used this letter already,'
                                'try again'.center(width))
        else:
            print(Fore.RED + 'Unrecognized character'
                             'try again with letter!'.center(width))
    tri(tries, word)
   

def tri(tries, word):   
    if tries == 0:
        clear()
        print(Fore.RED + (f'Sorry {name} you lost!!!').center(width))
        print(f'The word we were looking for was {word}'.center(width))
        print(hangman_as[tries])
        end_game()
 
    else:
        clear()
        text_win = pyfiglet.figlet_format(f'Well done {name}, you won!'.center(
            width))
        print(text_win)
        end_game()


def end_game():
    """
    Function that will ask user if he wants to play again.
    """
    while True:
        print('Would you like to play again?\n')
        again = input('Y/N?\n'.center(width)).upper()
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
                raise ValueError('\nYou must type Y or N.'.center(width))
        except ValueError as e_rr:
            print(Fore.RED + (f'Try again: {e_rr}'))


def thank_you():
    """
    This function will just print text for user
    when he decided to stop playing game
    """
    clear()
    thank_text = pyfiglet.figlet_format(f'Thank you for playing game {name}!')
    print(thank_text)


if __name__ == '__main__':
    welcome_screen()
    game()
