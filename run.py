import random
import string
import os
import pyfiglet
from pyfiglet import Figlet
from hangman import hangman_as
from words import word_list


def welcome():
    """
    Function to welcome screen which will provide user
    with rules and input field for his name.
    """
    # ascii_banner = pyfiglet.figlet_format("Welcome   to   HANGMAN!!!")
    # print(ascii_banner)
    # print("\n")
    # print("You play the game by guessing letters")
    # print("that makes hidden word. With each wrong")
    # print("guess you are one step closer to beeing")
    # print("hanged! You can choose between 3 levels")
    # print("but for start lets get your name first....")
    # print("\n")

    while True:
        name = input("Please enter your name:\n").strip().capitalize()

        if not name.isalpha():
            print("Name must be alphabets only!!!\n")
            
        else:
            clear()
            # levels()
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
    name = welcome()
    print(f'{name} Hello lets pick level for you!!!')
    while True:
        try:
            difficulty = input('Please type E for easy, M for medium or H for hard!').strip().upper()
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
                raise ValueError('Please type E or M or H for difficulty level!\n')
        except ValueError as e_rr:
            print(f"Invalid input:{e_rr}")
        
    return lives


def game():
    word = get_word(word_list)
    hidden_word = set(word)
    letter_alphab = set(string.ascii_uppercase)
    used_letters = set()
    tries = levels()

    while len(hidden_word) > 0 and tries > 0:
        print(' you have {tries} left for this round')
        print('You used:', ' '.join(used_letters))
        letter_words = [letter if letter in used_letters else '-' for letter in word]

        print(hangman_as[tries])
        print('Current word is:', ' '.join(letter_words))

        user_guess = input('Try to guess letter: \n').upper()

        if user_guess in letter_alphab - used_letters:
            clear()
            used_letters.add(user_guess)
            if user_guess in hidden_word:
                clear()
                hidden_word.remove(user_guess)
            else:
                clear()
                tries -= 1
                print('Your guess is not in the work, try again!')
        elif user_guess in used_letters and len(user_guess) != 1:
            clear()
            print('You used this letter already, try again')
        else:
            clear()
            print('Unrecognized character, please try again with letter!')
    if tries == 0:
        clear()
        custom_fig = Figlet(font='graffiti')
        print(custom_fig.renderText('Sorry you lost!!!'))
        print(f'The word we were looking for was {word}')
        print(hangman_as[tries])
        end()

    else:
        clear()
        print('Well done, you won!!!')
        end()


def end():
    """ Function that will ask user if he wants to play again.
    """
    while True:
        again = input('Would you like to play again? \n Y/N?\n').upper()
        try:
            if again == 'Y':
                clear()
                welcome()
                break
            elif again == "N":
                clear()
                thank_you()
                break
            else:
                raise ValueError(f'You must type Y or N. You typed {again}')
        except ValueError as e:
            print(f'Try again: {e}')


def thank_you():
    clear()
    print(
        """
         ,--.--------.  ,--.-,,-,--,   ,---.      .-._        ,--.-.,-.                         _,.---._                 
        /==/,  -   , -\/==/  /|=|  | .--.'  \    /==/ \  .-._/==/- |\  \        ,--.-.  .-,--.,-.' , -  `.  .--.-. .-.-. 
        \==\.-.  - ,-./|==|_ ||=|, | \==\-/\ \   |==|, \/ /, /==|_ `/_ /       /==/- / /=/_ //==/_,  ,  - \/==/ -|/=/  | 
        `--`\==\- \   |==| ,|/=| _| /==/-|_\ |  |==|-  \|  ||==| ,   /        \==\, \/=/. /|==|   .=.     |==| ,||=| -| 
            \==\_ \  |==|- `-' _ | \==\,   - \ |==| ,  | -||==|-  .|          \==\  \/ -/ |==|_ : ;=:  - |==|- | =/  | 
            |==|- |  |==|  _     | /==/ -   ,| |==| -   _ ||==| _ , \          |==|  ,_/  |==| , '='     |==|,  \/ - | 
            |==|, |  |==|   .-. ,\/==/-  /\ - \|==|  /\ , |/==/  '\  |         \==\-, /    \==\ -    ,_ /|==|-   ,   / 
            /==/ -/  /==/, //=/  |\==\ _.\=\.-'/==/, | |- |\==\ /\=\.'         /==/._/      '.='. -   .' /==/ , _  .'  
            `--`--`  `--`-' `-`--` `--`        `--`./  `--` `--`               `--`-`         `--`--''   `--`..---'   
      """
    )


welcome()
game()


# def hangman():
#     """
#     Functions to call other functions
#     """

#     welcome()
#     game(word_list, lives)


# hangman()