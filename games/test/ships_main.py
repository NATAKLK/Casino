import random
import os
import time

MAX_NPC_SHIPS = 5

ship_name_list = ["Hera","Prometeo","Afrodita","Apolo","Atenea","Ares","Poseidon","Odin","Hermes","Zeus","Cronos","Aquiles","Perceo","Artemisa","Deimos","Odiseo","Ades"]
ship_num = len(ship_name_list)
ship_selected = ""

class Ship:
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number
        self.progress = 0.0
    @staticmethod
    def random():
        name = random.choice(ship_name_list)
        number = random.randint(1, max(1, len(ship_name_list)))
        progress = 0.0
        return Ship(name, number)

def ship_art():
    print("""
                o
               |\\
        <\\____|##\\___
           .'~-~._~-/

    """)
 
def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def ship_select():
    global selected_ship
    selection = True
    while selection == True:
        clean_screen()
        print("----- Escoje al Barco que deseas apostar -----")
        for number, name in enumerate(ship_name_list, 1):
            print(f"{number}) {name}") 
        print("Seleccione el número de su Barco:")

        try:
            choice = int(input("> "))
            current_max = len(ship_name_list)
            if choice <= current_max and choice > 0:
                selected_ship = ship_name_list.pop(choice - 1)
                time.sleep(1)
                clean_screen()
                print(f"Has seleccionado al Barco: {selected_ship}")
                
                selection = False
                time.sleep(2)
                clean_screen()
                time.sleep(1)
                ship_game()

            else:
                clean_screen()
                print("Número inválido. Por favor, elige un número válido.")
                time.sleep(2)
                continue

        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
            time.sleep(2)
            continue

def create_npcs():
    list_ship_create: list[Ship] = []
    for i in range(MAX_NPC_SHIPS):
        list_ship_create.append(Ship.random())
        if list_ship_create[-1].name in ship_name_list:
            ship_name_list.remove(list_ship_create[-1].name)
    print("\Barcos en la carrera:")
    for i, ship in enumerate(list_ship_create, 1):
        print(f"Barco {i}: {ship.name}")
        time.sleep(2)
    print("Barco 8: " + selected_ship + " (Tu Barco)")
    list_ship_create.append(Ship(selected_ship, 8))
    time.sleep(2)
    clean_screen()

    return list_ship_create

def ship_game():
    # Hacer una lista de los Barcos ya generados.
    # Ir agregandole 1.0,1.5,0.5 de progreso a un Barco ALETORO y sucesivamente.
    # Repetir ese ciclo hasta que un Barco llegue a 100.0 de progreso.
    print("¡La carrera de barcos ha comenzado!")

    list_ship_create = create_npcs()
    while True:
        clean_screen()
        for ship in list_ship_create:
            print(f"{ship.name}: {ship.progress:.2f}")
        time.sleep(0.5)
        ship_progress_select = random.choice(list_ship_create)
        ship_progress_select_porcent = random.uniform(3.5,5.0)
        ship_progress_select.progress += ship_progress_select_porcent
        if ship_progress_select.progress >= 100.0:
            #ship_progress_select = ship_progress_select.name
            if ship_progress_select_porcent >= 100.0:
                print(f""" 
            ------ Felicidades tu barco ha ganado ------
             Ganó {ship_progress_select.name} con un progreso de {ship_progress_select.progress:.2f} 
""")
                break
            else:
                print(f"""
                ------ Suerte a la proxima, tu barco NO ha ganado! ------
                Ganó {ship_progress_select.name} con un progreso de {ship_progress_select.progress:.2f} 

""")
                break

        else:
            continue

# Mas interactividad en el juego:
#   - Que al hacer click, enviar una letra u cualquier otra cosa, que vaya aumentando la forma ne la que puedas ganar

    

"""
    while ship_create[-1].progress < 100.0:
        for ship in ship_create:
            ship.progress += random.uniform(0.5, 2.0)
            if ship.progress >= 100.0:
                ship.progress = 100.0
                break
        time.sleep(1)
        clean_screen()
        print("Progreso de la carrera:")
        ship_race = True
        for ship in ship_create:
            print(f"{ship.name}: {ship.progress:.2f}%")
            if ship.progress >= 100.0:
                print(f"\n¡El barco {ship.name} ha ganado la carrera!")
"""     
        



# quiero acceder y poner un while a el progreso de la clase Ship, pero antes genere 7 randoms y lo guarde en la lista ship_create, como hacer ese while