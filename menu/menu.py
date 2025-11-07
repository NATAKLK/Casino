from rich.console import Console
from rich.align import Align
from rich.panel import Panel
from rich.text import Text
from rich.layout import Layout
from games.ships import *
import os
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
    menu_text.append("(5) SALIR", style="red")
    menu_text.append("\n")

    # Create panel with aligned text
    panel = Panel(
        Align.center(menu_text),
        border_style="red",
        title="Casino",
        padding=(10, 4),
        height=terminal_height - 4,  # Ajustamos la altura del panel
        width=terminal_width // 2    # Hacemos el panel la mitad del ancho de la terminal
    )

    # Clear screen
    console.clear()
    
    # Print centered panel usando Align.center para centrar el panel completo
    console.print(Align.center(panel))

    choice = int(input("\nPlease select an option (1-5): "))
    if choice  == 1:
        ship_select()
    


