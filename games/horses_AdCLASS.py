import random
import os
import time

horse_name_list = ["Hera","Prometeo","Afrodita","Apolo","Atenea","Ares","Poseidon","Odin","Hermes","Zeuz","Cronos","Aquiles","Perceo","Artemisa","Deimos"]

class Horse:
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number
        self.progress = 0.0

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def horse_select():
    print("----- Escoje al caballo que deseas apostar -----")
    for number, name in enumerate(horse_name_list, 1):
        print(f"{number}) {name}") 
    print("Seleccione el número de su caballo:")
    try:
        choice = int(input("> "))
        if 1 <= choice <= len(horse_name_list):
            selected_horse = horse_name_list[choice - 1]
            print(f"Has seleccionado al caballo: {selected_horse}")
        else:
            clean_screen()
            print("Número inválido. Por favor, elige un número válido.")
            time.sleep(2)
            horse_select
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")
    
    horse_
    for i in 
    pancho = Horse("Pancho", 1)
    print(pancho.progress)

