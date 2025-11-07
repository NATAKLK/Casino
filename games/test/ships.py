from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
import random
import os
import time
from typing import List

console = Console()

MAX_NPC_SHIPS = 3
TRACK_LENGTH = 170  # longitud del track en caracteres

ship_name_list = ["Hera","Prometeo","Afrodita","Apolo","Atenea","Ares","Poseidon","Odin","Hermes","Zeus","Cronos","Aquiles","Perceo","Artemisa","Deimos","Odiseo","Ades"]
ship_num = len(ship_name_list)
selected_ship = ""


class Ship:
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number
        self.progress = 0.0

    @staticmethod
    def random_from_list(names: List[str], number: int):
        name = random.choice(names) if names else f"NPC{number}"
        return Ship(name, number)


def ship_art(ship: Ship, track_length: int = TRACK_LENGTH) -> Panel:
    """
    Dibuja el barco desplazado según ship.progress.
    """
    pct = max(0.0, min(ship.progress, 100.0))
    pos = int((pct / 100.0) * track_length)
    indent = " " * pos

    # ASCII art del barco orientado a la derecha
    art_lines = [
        indent + "   o",
        indent + "  /|\\",
        indent + " /_|_\\__/>"
    ]

    # Línea final del track y meta
    finish = " " * track_length + " |META|"

    art = "\n".join(art_lines + [finish])
    title = f"{ship.name} — {ship.progress:.1f}%"
    style = "bold red" if ship.name == selected_ship else "cyan"
    return Panel(art, title=title, padding=(0, 1), border_style=style)


def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def play_ships():
    global selected_ship
    while True:
        clean_screen()
        console.print(Panel.fit("[yellow]CARRERA DE BARCOS[/yellow]", border_style="bold yellow"))
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Número", style="dim", width=6)
        table.add_column("Nombre del Barco", style="cyan")

        for number, name in enumerate(ship_name_list, 1):
            table.add_row(str(number), name)

        console.print(table)
        console.print("\n[bold cyan]Seleccione el número de su Barco:[/bold cyan]")

        try:
            choice = int(input("> "))
            current_max = len(ship_name_list)
            if 1 <= choice <= current_max:
                selected_ship = ship_name_list.pop(choice - 1)
                time.sleep(1)
                clean_screen()
                console.print(f"Has seleccionado al Barco: [bold yellow]{selected_ship}[/bold yellow]")
                time.sleep(1)
                clean_screen()
                ship_game()
                return
            else:
                console.print("[red]Número inválido. Intenta de nuevo.[/red]")
                time.sleep(1)
        except ValueError:
            console.print("[red]Entrada inválida. Ingresa un número.[/red]")
            time.sleep(1)


def create_npcs() -> List[Ship]:
    """
    Crea NPCs sin repetir nombres y añade el barco del jugador al final.
    """
    list_ship_create: List[Ship] = []
    available_names = ship_name_list.copy()

    for i in range(MAX_NPC_SHIPS):
        if available_names:
            name = random.choice(available_names)
            available_names.remove(name)
            s = Ship(name, i + 1)
        else:
            s = Ship.random_from_list([], i + 1)
        list_ship_create.append(s)

    # Añadir el barco del jugador (si existe) con número final
    player_name = selected_ship if selected_ship else "Jugador"
    list_ship_create.append(Ship(player_name, MAX_NPC_SHIPS + 1))
    return list_ship_create


def ship_game():
    console.print(Panel.fit("[bold yellow]¡La carrera de barcos ha comenzado![/bold yellow]", border_style="yellow"))
    list_ship_create = create_npcs()
    time.sleep(0.8)

    # Bucle principal de la carrera
    while True:
        clean_screen()

        # Ordenar por progreso (mayor primero) para que el primero se muestre arriba
        list_ship_create.sort(key=lambda s: s.progress, reverse=True)

        # Mostrar cada barco usando ship_art
        for ship in list_ship_create:
            console.print(ship_art(ship))

        time.sleep(0.2)

        # Actualizar progreso: varios incrementos para dinamismo
        for _ in range(2):
            ship_progress_select = random.choice(list_ship_create)
            ship_progress_select_porcent = random.uniform(0.5, 3.0)
            ship_progress_select.progress = min(100.0, ship_progress_select.progress + ship_progress_select_porcent)

        # Comprobar ganador
        winners = [s for s in list_ship_create if s.progress >= 100.0]
        if winners:
            # Determinar ganador real (mayor progreso)
            winner = max(winners, key=lambda s: s.progress)
            clean_screen()
            if winner.name == selected_ship:
                clean_screen()
                console.print(Panel.fit(
                    f"[bold green]¡FELICIDADES! ¡TU BARCO HA GANADO![/bold green]\n\n"
                    f"[yellow]{winner.name}[/yellow] — {winner.progress:.1f}%",
                    border_style="green"
                ))
            else:
                clean_screen()
                console.print(Panel.fit(
                    f"[bold red]¡MEJOR SUERTE LA PRÓXIMA VEZ![/bold red]\n\n"
                    f"Ganó [yellow]{winner.name}[/yellow] — {winner.progress:.1f}%",
                    border_style="red"
                ))
            break