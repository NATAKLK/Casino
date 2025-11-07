from rich.console import Console
from rich.align import Align
from rich.panel import Panel
from rich.text import Text
from rich.layout import Layout
from games.test.ships import *
from games.blackjack import *
from games.hangman import *
from games.roulette import *
import os
from extras.utils import *
import shutil

console = Console()
def menu_principal():
    # Obtener dimensiones de la terminal
    terminal_width, terminal_height = shutil.get_terminal_size()

    # Create menu text with colors
    print()
    menu_text = Text()
    menu_text.append("\n")
    menu_text.append("Menu Principal", style="bold red blink")
    menu_text.append("\n\n")
    menu_text.append("(1) Juegos\n\n", style="cyan")
    menu_text.append("(2) Estadisticas\n\n", style="cyan")
    menu_text.append("(3) Reglas de juegos\n\n", style="cyan")
    menu_text.append("(4) Banco\n\n", style="cyan")
    menu_text.append("--------------------\n", style="white")
    menu_text.append("(5) Close", style="red")
    menu_text.append("\n")

    # Create panel with aligned text
    panel = Panel(
        Align.center(menu_text),
        border_style="red",
        title="Casino",
        padding=(10, 4),
        height=terminal_height - 4,  # Ajustamos la altura del panel
        width=terminal_width // 3    # Hacemos el panel la mitad del ancho de la terminal
    )

    # Clear screen
    clean_screen()
    
    # Print centered panel usando Align.center para centrar el panel completo
    console.print(Align.center(panel))

    try:
        console.print("\nPlease select an option (1-5): ", style ="bold cyan blink")
        choice = int(input())
        if choice == 1:
            menu_games()
        elif choice == 2:
            clean_screen()
            console.print("On building, please be patient. Tanks!", style ="bold red blink")
            time.sleep(2)
            menu_principal()
        elif choice == 3:
            clean_screen()
            console.print("On building, please be patient. Tanks!", style ="bold red blink")
            time.sleep(2)
            menu_principal()
        elif choice == 4:
            clean_screen()
            console.print("On building, please be patient. Tanks!", style ="bold red blink")
            time.sleep(2)
            menu_principal()
        elif choice == 5:
            clean_screen()
            console.print("Tnks for playing!", style="bold blue blink")
        else:
            clean_screen()
            console.print("\nPlease select an option (1-5): ", style ="bold cyan blink")
            time.sleep(2)
            clean_screen()
            menu_principal()
    except ValueError:
        clean_screen()
        console.print("\nPlease select an option (1-5): ", style ="bold cyan blink")
        clean_screen()
        menu_principal()


    
def menu_games():
    # Obtener dimensiones de la terminal
    terminal_width, terminal_height = shutil.get_terminal_size()

    # Create menu text with colors
    print()
    menu_text = Text()
    menu_text.append("\n")
    menu_text.append("Menu Principal", style="bold red blink")
    menu_text.append("\n\n")
    menu_text.append("(1) Ships\n\n", style="cyan")
    menu_text.append("(2) Blackjack\n\n", style="cyan")
    menu_text.append("(3) HangMan\n\n", style="cyan")
    menu_text.append("(4) Roulette\n\n", style="cyan")
    menu_text.append("--------------------\n", style="white")
    menu_text.append("(5) SALIR", style="red")
    menu_text.append("\n")

    panel_games = Panel(
        Align.center(menu_text),
        border_style="bold cyan blink",
        title="Games",
        padding=(10, 4),
        height=terminal_height - 3,  # Ajustamos la altura del panel
        width=terminal_width // 3    # Hacemos el panel la mitad del ancho de la terminal
    )

    console.print(Align.center(panel_games))

    try:
        console.print("\nPlease select an option (1-5): ", style ="bold cyan blink")
        choice = int(input())
        if choice == 1:
            clean_screen()
            console.print("On building, please be patient. Tanks!", style ="bold red blink")
            time.sleep(2)
            menu_games()
        elif choice == 2:
            play_blackjack()
        elif choice == 3:
            clean_screen()
            console.print("On building, please be patient. Tanks!", style ="bold red blink")
            time.sleep(2)
            menu_games()
        elif choice == 4:
            clean_screen()
            console.print("On building, please be patient. Tanks!", style ="bold red blink")
            time.sleep(2)
            menu_games()
        elif choice == 5:
            clean_screen()
            menu_principal()
        else:
            clean_screen()
            console.print("\nPlease select an option (1-4): ", style ="bold cyan blink")
            time.sleep(2)
            clean_screen()
            menu_games()
    except ValueError:
        clean_screen()
        console.print("\nPlease select an option (1-4): ", style ="bold cyan blink")
        clean_screen()
        menu_games
        
    


