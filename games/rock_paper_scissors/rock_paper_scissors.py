import random
import os 

ppt_options = ["Piedra","Papel","Tijera"]
user_selection = []
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_question():
    clear_console()
    print("""
    ¿Quieres jugar PIEDRA, PAPEL o TIJERA?
          (1) Si
          (2) No
          """)
    choice = input("> ").lower()
    if choice in ("1","yes","si","s","y"):
        clear_console()
        play_game()
    elif choice in ("2","no","n","nou"):
        print("Vuelve pronto!")
    else:
        input("Opcion incorrecta, presiona ENTER para continuar...")
        clear_console()
        play_question()
        
def play_game():
    user_selection.clear()
    print(""""
    ¿Cuál es tu elección?
        (1) Piedra
        (2) Papel
        (3) Tijera
          """)
    choice = input("> ").lower()
    if choice in ("1","piedra","rock","r"):
        user_selection.append("Piedra")
        clear_console()
        condicion_game()
    elif choice in ("2","papel","paper","p"):
        user_selection.append("Papel")
        clear_console()
        condicion_game()
    elif choice in ("3","tijera","scissors","s"):
        user_selection.append("Tijera")
        clear_console()
        condicion_game()
    return user_selection

def condicion_game():
    machine_selection = random.choice(ppt_options)
    current_user_choice = user_selection[0]

    print(f"Tu elegiste: {user_selection}")
    print(f"La maquina eligio: {machine_selection}")

    if machine_selection == current_user_choice:
        print(f"\n¡Empate! Ambos eligieron {machine_selection}")

    elif (machine_selection == "Piedra" and current_user_choice == "Papel") or \
         (machine_selection == "Papel" and current_user_choice == "Tijera") or \
         (machine_selection == "Tijera" and current_user_choice == "Piedra"):
        print(f"\n¡Ganaste! {current_user_choice} vence a {machine_selection}")

    else:
        print(f"\n¡Perdiste! {machine_selection} vence a {current_user_choice}")
        
    input("\nPresiona ENTER para volver al menu...")
    play_question()

play_question()