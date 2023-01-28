import random
import string
import os
import datetime
import gspread
import pyfiglet
from google.oauth2.service_account import Credentials
from tabulate import tabulate
from colorama import Fore, init, Style
from hangman import hangman_as
from words import word_list
init(autoreset=True)
width = os.get_terminal_size().columns

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('score')

leaders = SHEET.worksheet('leaderboard')
date = datetime.datetime.now().strftime("%d-%m-%Y")


def welcome_screen():
    """
    Function to welcome screen which will provide user
    with rules and input field for his name.
    """
    welcome_text = pyfiglet.figlet_format('** Hangman **')
    print(welcome_text)
    global name
    while True:
        print('\n')
        print("\n")
        name = (
            input(
                Fore.MAGENTA
                + Style.BRIGHT
                + ("Please enter your name:\n".center(width))
            )
            .strip()
            .capitalize()
        )
        print("\n")
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
    welcome_text = pyfiglet.figlet_format('**Hangman**')
    print(welcome_text)
    print("\n")
    print(Fore.LIGHTWHITE_EX + "Rules of this game are fairly"
                               " simple!!!\n".center(width))
    print("1. You are guessing letters one by one that makes"
          " hidden word.".center(width))
    print("2. With each wrong guess you are"
          " losing a life and 1 point from score".center(width))
    print("3. With each right guess you are"
          " getting closer to win and 1 point from score".center(width))
    print("4. How many lives you have depends on the level you chose".center(
        width))
    print("5. You win by guessing all the letters in the"
          " word and getting extra 10 points".center(width))
    print(Fore.LIGHTYELLOW_EX + "HARD =3 tries, MEDIUM ="
                                "5 tries, EASY =7 tries\n".center(width))
    while True:
        try:
            pas_b = input(
                Fore.LIGHTWHITE_EX + ("Type P to"
                                      " play the game:\n".center(width))
            ).upper()
            if pas_b == "P":
                levels()
                break
            else:
                clear()
                raise ValueError(Fore.RED + ("Please type letter P!!!"))
        except ValueError as e_rr:
            print(f"Invalid input:{e_rr}")


def check_rules():
    """
    This function will check if user wish to read rules or continue with game!
    """
    clear()
    welcome_text = pyfiglet.figlet_format('**Hangman**')
    print(welcome_text)
    print('\n')
    print(f"{Fore.BLUE + Style.BRIGHT} What a lovely name {name}!\n".center(
        width))
    print("If you wish to read rules press R,to continue press C!!".center(
        width))
    while True:
        try:
            check = input('Press (R)ules or (C)ontinue:\n'.center(
                    width)).upper()
            if check == 'R':
                rules()
                break
            elif check == 'C':
                levels()
                break
            else:
                clear()
                raise ValueError(
                    Fore.RED + ('Please choose letters R or C!'))
        except ValueError as e_rr:
            print(f"Invalid input:{e_rr}")
    clear()


def levels():
    """
    This function will ask player to choose dificulty level for the game.

    """
    global lives
    clear()
    print(f'{name}, now choose your level!'.center(width))
    print('\n')
    while True:
        try:
            print(Fore.GREEN + 'Please type E for easy\n'.center(width))
            print(Fore.CYAN + 'Please type M for medium\n'.center(width))
            print(Fore.YELLOW + 'Please type H for hard\n'.center(width))
            difficulty = input(''.center(width)).strip().upper()
            if difficulty == 'E':
                lives = 7
                break
            elif difficulty == 'M':
                lives = 5
                break
            elif difficulty == 'H':
                lives = 3
                break
            else:
                clear()
                raise ValueError(
                    Fore.RED + ('Please type E, M or H!!!'))
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
    global score
    word = get_word()
    hidden_word = set(word)
    letter_alphab = set(string.ascii_uppercase)
    used_letters = set()
    tries = lives
    points = 0
    score = 0

    while len(hidden_word) > 0 and tries > 0:
        print(f'{Fore.WHITE + Style.BRIGHT}Your score: {points}')
        letter_words = \
            [letter if letter in used_letters else '-' for letter in word]
        print(hangman_as[tries])
        print(' '.join(letter_words).center(width))
        print(
            Fore.MAGENTA
            + Style.BRIGHT
            + (f"{name} you have {tries} lives left for this round")
        )
        print('You used:', ' '.join(used_letters))

        user_guess = input(Fore.LIGHTWHITE_EX + Style.BRIGHT + "Try"
                           " to guess letter:\n".center(width)).upper()
        clear()
        if user_guess in letter_alphab - used_letters:
            used_letters.add(user_guess)
            if user_guess in hidden_word:
                hidden_word.remove(user_guess)
                points += 1
            else:
                tries -= 1
                points -= 1
                print(Fore.RED + 'Your guess is not in the word,'
                                 'try again!'.center(width))
        elif user_guess in used_letters:
            print(Fore.YELLOW + 'You used this letter already,'
                                'try again'.center(width))
        else:
            print(Fore.RED + 'Unrecognized character'
                             ' try again with letter!'.center(width))
    if tries == 0:
        clear()
        print(Fore.RED + (f'Sorry {name} you lost!!!\n').center(width))
        print('The word we were looking for was:'.center(width))
        print(f"{Fore.YELLOW + Style.BRIGHT} {word}".center(width))
        print(hangman_as[tries])
        print(f"{Fore.WHITE + Style.BRIGHT}Your score was: {score}".center(
            width))
        print("\n")
        update_scoreboard()
        end_game()

    else:
        clear()
        score = points + 10
        update_scoreboard()
        print(Fore.BLUE
              + Style.BRIGHT + (f" Well done {name}, you won!").center(width))
        print(
            """
                                   .-''.
                                  /    \\
                             ')  || '/' | (`
                              \\  \\`_.' //
                               \\.-`--'.//
                                 Y .  .Y
                                 | . . |
                                 |     |
                                 ||' '||
                                 ||   ||
                              __//     \\__
        """)
        print(f"{Fore.WHITE + Style.BRIGHT}Your score was: {score}".center(
            width))
        end_game()


def end_game():
    """
    Function that will ask user if he wants to play again.
    """
    clear()
    while True:
        print(f"{Fore.GREEN + Style.BRIGHT} {name} you can play again, check"
              " leaderboard or exit game.\n".center(
                width))
        again = input('Press (Y)es, (N)o or (S)core:\n'.center(width)).upper()
        try:
            if again == 'Y':
                clear()
                levels()
                game()
                break
            elif again == "N":
                clear()
                thank_you()
                break
            elif again == "S":
                clear()
                leader_board()
                break
            else:
                clear()
                raise ValueError('\nYou must type Y,N or S!!!'.center(width))
        except ValueError as e_rr:
            print(Fore.RED + (f'Try again: {e_rr}'))


def thank_you():
    """
    This function will just print text for user
    when he decided to stop playing game
    """
    thank_text = pyfiglet.figlet_format(f'Thank you for playing game {name}!')
    print(thank_text)


def update_scoreboard():
    """
    Function to update data on google sheets
    """
    update = [name, score, date]
    leaders.insert_row(update, 3)


def leader_board():
    """
    Function to display scores on user request
    """
    clear()
    leaders.sort((2, 'des'))
    data = leaders.get("A2:C10")
    # print(data)
    print(tabulate(data, headers=['name', 'score', 'date']))
    while True:
        print("\n")
        print(Fore.GREEN
              + Style.BRIGHT
              + "Hope you are happy with your score,"
                " now lets get you back!".center(width))
        print("\n")
        back = input("Press (B)ack:\n".center(width)).upper()
        try:
            if back == 'B':
                clear()
                end_game()
                break
            else:
                clear()
                raise ValueError('\nYou must type B!!!'.center(width))
        except ValueError as e_rr:
            print(Fore.RED + (f'Try again: {e_rr}'))


if __name__ == '__main__':
    welcome_screen()
    check_rules()
    game()
