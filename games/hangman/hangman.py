# El juego del ahoracado con una lista básica de palabras
import random
from extras.utils import *
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
import os
import time
from games.hangman.hangman_utils import *

console = Console()
#                               _ _ _ _ _ _


def play_hangman():
    word_choice = random.choice(WORD_LIST_EN_PROGRAM)
    wrong = 1
    cantidad_letras = len(word_choice)
    MAX_WRONG = 7
    guees_word = ["_"] * len(word_choice)

    while "_" in guees_word:
        console.print("Introduce la Palabra / Letra que deseas usar", style="bold cyan")
        
        choice = str(input())
        
        
        for i in range(len(word_choice)):
                if choice == word_choice[i]:
                    guees_word[i] = choice

        for w in guees_word:
            print(w, end=" ")
        
        print()

        if not choice in word_choice:
            print(HANGMAN_PICS[wrong])
            wrong += 1
            if wrong == MAX_WRONG:
                console.print("Haz llegado al maximo de letras", style="blink red")
                console.print(f"La palabra correcta era: {word_choice}", style="bold green")
                time.sleep(3)
                break
            continue
    clean_screen()

def hangman_select_word():
     clean_screen()
     console.print("",style="")