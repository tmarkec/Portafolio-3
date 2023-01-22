import random
import string
import os
import pyfiglet
from pyfiglet import Figlet
from hangman import hangman_as


def welcome():
    """Welcome screen which will provide user
       with rules and input field for his name
    """
    ascii_banner = pyfiglet.figlet_format("Welcome   to   HANGMAN!!!")
    print(ascii_banner)
    print("\n")
    print("You play the game by guessing letters")
    print("that makes hidden word. With each wrong")
    print("guess you are one step closer to beeing")
    print("hanged! You can choose between 3 levels")
    print("but for start lets get your name first")
    print("\n")


welcome()