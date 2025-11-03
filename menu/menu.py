from rich.console import Console
from rich.align import Align
from rich.panel import Panel
from rich.text import Text
import shutil
import os

console = Console()

def menu_principal():
    # Create menu text with colors
    menu_text = Text()
    menu_text.append("\n\n")
    menu_text.append("Menu Principal", style="bold red blink")
    menu_text.append("\n\n")
    menu_text.append("(1) Juegos\n\n", style="cyan")
    menu_text.append("(2) Estadisticas\n\n", style="cyan")
    menu_text.append("(3) Reglas de juegos\n\n", style="cyan")
    menu_text.append("(4) Banco\n\n", style="cyan")
    menu_text.append("--------------------\n", style="white")
    menu_text.append("(5) SALIR", style="red")
    menu_text.append("\n\n")

    # Create panel with aligned text
    panel = Panel(
        Align.center(menu_text),
        border_style="red",
        title="Casino",
        padding=(2, 4)
    )

    # Clear screen first (optional)
    console.clear()
    
    # Print centered panel
    console.print(Align.center(panel, vertical=True))

    choice = input("\nPlease select an option (1-5): ")
    return choice

