
from extras.utils import *
import shutil
import os

def menu_principal():
    list_colors()
    print(f"""
*------------------------------------------*#



                 ----
            {RED_BRIGHT}{BLINK}{UNDERLINE}M{RESET}{BLINK}{UNDERLINE}e{RED_BRIGHT}n{RESET}{BLINK}{UNDERLINE}u {RED_BRIGHT}P{RESET}{BLINK}{UNDERLINE}r{RED_BRIGHT}i{RESET}{BLINK}{UNDERLINE}n{RED_BRIGHT}c{RESET}{BLINK}{UNDERLINE}i{RED_BRIGHT}{BLINK}{UNDERLINE}p{RESET}{BLINK}{UNDERLINE}a{RED_BRIGHT}l{RESET}
                 ----
            
    (1)        Juegos 

    (2)     Estadisticas

    (3)    Reglas de juegos

    (4)        Banco

                 ----
    
    (5)        SALIR
                
*------------------------------------------*


""")
    cols, rows = shutil.get_terminal_size()
    lines = menu_principal.splitlines()
    top_pad = max(0, (rows - len(lines)) // 2)

    print("\n" * top_pad, end="")
    for line in lines:
        print(line.center(cols))
    choice = input("Please select an option (1-3): ")
    return choice

