import random
import os

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def horse_selection():
    horse_election = True
    while horse_election:
        print("----- Selección de Caballos -----")
        print("Caballos disponibles:")
        print("1. Horse1")
        print("2. Horse2")
        print("3. Horse3")
        print("4. Horse4")
        print("5. Horse5")
        print("6. Horse6")
        print("7. Horse7")
        print("8. Horse8")
        print("Elige el caballo que deseas seleccionar (1-8)")
        try:
            choice = int(input(">"))
            if choice in (1,2,3,4,5,6,7,8):
                horse_election = False
                clean_screen()
                race()
                
            else:
                clean_screen()
                print("Elige una opcion correcta")
        except ValueError:
            clean_screen()
            print("Elige una opcion correcta")

def race():
    time.sleep(2)
    num_horses =8

    horses = []

    for i in range(1, num_horses):
        horses.append(f"Horse{i}")

    print(horses)


horse_selection()