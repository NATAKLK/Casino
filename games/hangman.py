# El juego del ahoracado con una lista básica de palabras
import random
from extras.utils import *
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
import random
import os
import time

console = Console()
#                               _ _ _ _ _ _
WORD_LIST = [
    "python","casino","..."
]

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ======="""
]

def word_selection():
    random.choice(WORD_LIST)

def play_hangman():
    word_choice = word_selection()
    wrong = 0
    max_wrong = 7
    gress_word = []
    while True:
        clean_screen()
        console.print("Introduce la Palabra / Letra que deseas usar", style="bold cyan")
        
        choice = str(input())
        try:
            if ...:
                ...
            elif choice in ("1","2","3","4","5","6","7","8","9","0"):
                console.print("Elige una letra del abecedario correcta", style="bold blue")
                continue
            else:
                console.print("Es coje una letra del abecedario", style="bold blue")
                continue
        except ValueError:
            continue


