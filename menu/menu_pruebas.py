# ...existing code...
from extras.utils import *
import os
import shutil

def title_print():
    return f"{RED_BRIGHT}{BLINK}{UNDERLINE}M{RESET}{BLINK}{UNDERLINE}e{RED_BRIGHT}n{RESET}{BLINK}{UNDERLINE}u {RED_BRIGHT}P{RESET}{BLINK}{UNDERLINE}r{RED_BRIGHT}i{RESET}{BLINK}{UNDERLINE}n{RED_BRIGHT}c{RESET}{BLINK}{UNDERLINE}i{RED_BRIGHT}{BLINK}{UNDERLINE}p{RESET}{BLINK}{UNDERLINE}a{RED_BRIGHT}l{RESET}"

def menu_principal():
    list_colors()

    menu = f"""
──────────────────────────────────────────

────
{title_print()}
────

(1) Juegos 

(2) Estadisticas

(3) Reglas de juegos

(4) Banco

────

(5)SALIR
                
──────────────────────────────────────────
"""

    os.system('cls')  # Windows clear
    cols, rows = shutil.get_terminal_size(fallback=(80, 24)).columns, shutil.get_terminal_size(fallback=(80, 24)).lines
    lines = menu.splitlines()
    top_pad = max(0, (rows - len(lines)) // 2)

    print("\n" * top_pad, end='')
    for line in lines:
        print(line.center(cols))

    prompt = "Please select an option (1─3):"
    print(prompt.center(cols), end=' ')
    choice = input()
    return choice

# ...existing code...