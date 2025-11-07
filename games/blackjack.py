from enum import Enum
from extras.utils import *
import random
import time
import os

# =================================================================== Colores y Utilidades ===================================================================

# Colores ANSI para la terminal 
C_RESET = '\033[0m'
C_ROJO = '\033[91m'
C_AMARILLO = '\033[93m'
C_VERDE = '\033[92m'
C_CYAN = '\033[96m'

# ===================================================================== Cartas ======================================================================

class TypeCard(Enum):
    # Ahora guardamos una tupla: (Nombre, Símbolo, Color)
    HEARTS = ("Corazones", "♥", C_ROJO)
    DIAMONDS = ("Diamantes", "♦", C_ROJO)
    SPADES = ("Picas", "♠", C_RESET)  # C_RESET es el color por defecto (blanco/gris)
    CLUBS = ("Tréboles", "♣", C_RESET)

    @classmethod
    def random(cls):
        return random.choice(list(TypeCard))

class Card:
    def __init__(self, value: int = 0 , tipo: TypeCard = TypeCard.CLUBS, is_first: bool = False):
        self.value = value
        self.tipo = tipo
        self.is_first = is_first

    @property
    def rank_para_mostrar(self):
        """ Devuelve el string que se dibujará en la carta (A, 2-9, 10, J) """
        if self.value == 1:
            return "A"
        if self.value == 10:
            return "10"
        if self.value == 11:
            return "J"  # Asumimos que 11 es 'Jota'
        return str(self.value)

    @classmethod
    def random(cls):
        return Card(random.randint(1, 11), TypeCard.random(), False)
    
    def __repr__(self):
        # Usamos el nombre del palo (Ej: "Corazones")
        return f"Carta({self.value}, {self.tipo.value[0]}, {self.is_first})"

# ============================================================== Funciones de Dibujo ASCII ===============================================================

def get_arte_carta(carta: Card):
    """ Devuelve una lista de strings (líneas) para dibujar una sola carta. """
    
    rank = carta.rank_para_mostrar
    nombre, simbolo, color = carta.tipo.value  # Desempaquetamos la tupla
    
    # Ajustamos el padding para que '10' quepa bien
    if rank == "10":
        rank_izq = "10"
        rank_der = "10"
    else:
        rank_izq = f"{rank} "  # Ej: "A "
        rank_der = f" {rank}" # Ej: " A"

    # Devolvemos la lista de líneas, aplicando color
    return [
        f"{color}┌─────────┐{C_RESET}",
        f"{color}│{rank_izq}       │{C_RESET}",
        f"{color}│         │{C_RESET}",
        f"{color}│    {simbolo}    │{C_RESET}",
        f"{color}│         │{C_RESET}",
        f"{color}│       {rank_der}│{C_RESET}",
        f"{color}└─────────┘{C_RESET}"
    ]

def imprimir_cartas(cartas: list):
    """ Imprime una lista de objetos Card uno al lado del otro. """
    if not cartas:
        return

    # 1. Obtener el arte (lista de líneas) para cada carta
    artes_de_cartas = [get_arte_carta(carta) for carta in cartas]
    
    # 2. Asumir que todas las cartas tienen la misma altura
    altura_carta = len(artes_de_cartas[0]) # 7 líneas
    
    # 3. Imprimir línea por línea, horizontalmente
    for i in range(altura_carta):
        linea_para_imprimir = ""
        for arte in artes_de_cartas:
            linea_para_imprimir += arte[i] + "  "  # Añadir espacio entre cartas
        print(linea_para_imprimir)

# ====================================================================== Juego ======================================================================

def ask_play_again():
    print("\n--- ¿Jugar de nuevo? ---")
    print("      (Si / No)")
    
    while True:
        play_again = input("> ").lower()
        if play_again in ("yes", "si", "y", "s"):
            time.sleep(1)
            return True
        elif play_again in ("no", "n", "nou", "nah"):
            print("\n¡Hasta luego! Gracias por jugar.")
            return False
        else:
            print("Escoje una opcion válida (si/no).")

def play_blackjack():
    clean_screen()
    mano_user = []
    sum_user = 0
    user_playing = True

    print(f"{C_AMARILLO}--- 🃏 ¡Bienvenido al 21! 🃏 ---{C_RESET}")

    while user_playing:
        card_user = Card.random()
        mano_user.append(card_user)
        
        sum_user = sum(carta.value for carta in mano_user)

        clean_screen()
        print(f"{C_VERDE}¡Nueva carta!{C_RESET} Sacaste un {card_user.rank_para_mostrar} de {card_user.tipo.value[0]} {card_user.tipo.value[1]}")
        
        print("\nTu mano actual:")
        imprimir_cartas(mano_user)
        
        print(f"\n{C_AMARILLO}Total en tu mano: {sum_user}{C_RESET}")

        if sum_user > 21:
            print(f"\n{C_ROJO}¡Perdiste! Te pasaste de 21.{C_RESET}")
            user_playing = False
            break
        elif sum_user == 21:
            print(f"\n{C_VERDE}¡BLACKJACK! ¡Tienes 21!{C_RESET}")
            user_playing = False
            break

        while True:
            time.sleep(1)
            choice = input(f"\n{C_CYAN}¿Quieres sacar otra carta? (si/no):{C_RESET} ").lower()
            if choice in ("yes", "si", "y", "s"):
                break
            elif choice in ("no", "n", "nou", "nah"):
                user_playing = False
                break
            else:
                print("Introduce una respuesta correcta, 'SI' o 'NO'")
                continue

    # --- Turno de la Casa ---
    
    mano_house = []
    sum_house = 0

    if sum_user <= 21:
        clean_screen()
        print(f"{C_CYAN}--- Turno de la casa ---{C_RESET}")
        print("Tu mano final:")
        imprimir_cartas(mano_user)
        print(f"{C_AMARILLO}Tu total: {sum_user}{C_RESET}")
        print("\nLa casa está jugando...")
        time.sleep(2)
        
        while sum_house < 17 or sum_house < sum_user:
            card_house = Card.random()
            mano_house.append(card_house)
            sum_house = sum(carta.value for carta in mano_house)

            clean_screen()
            print(f"{C_CYAN}--- Turno de la casa ---{C_RESET}")
            print("Tu mano final:")
            imprimir_cartas(mano_user)
            print(f"{C_AMARILLO}Tu total: {sum_user}{C_RESET}")
            
            print("\nMano de la casa:")
            imprimir_cartas(mano_house)
            print(f"{C_AMARILLO}Total de la casa: {sum_house}{C_RESET}")
            
            time.sleep(2)
 
            if sum_house >= 17 and sum_house >= sum_user:
                 break
            if sum_house > 21:
                break
        
        print("\n--- 🏆 Resultados 🏆 ---")
        print(f"{C_VERDE}Tu puntuación: {sum_user}{C_RESET}")
        print(f"{C_ROJO}Puntuación de la casa: {sum_house}{C_RESET}\n")

        if sum_house > 21:
            print(f"{C_VERDE}¡Haz ganado!{C_RESET} La casa se pasó de 21.")
        elif sum_house > sum_user:
            print(f"{C_ROJO}Haz perdido.{C_RESET} La casa tiene una mano más alta.")
        elif sum_user > sum_house:
            print(f"{C_VERDE}¡Haz ganado!{C_RESET} Tu mano es más alta que la de la casa.")
        else: # sum_user == sum_house
            print(f"{C_AMARILLO}¡Empate!{C_RESET} Ambos tienen la misma puntuación.")
    
    elif sum_user > 21:
        print("\n--- 🏆 Resultados 🏆 ---")
        print(f"{C_ROJO}Tu puntuación: {sum_user}{C_RESET}")
        print(f"{C_ROJO}Haz perdido, te pasaste de 21.{C_RESET}")


# ======================================================================= Main ======================================================================

if __name__ == "__main__":
    while True:
        play_blackjack()
        time.sleep(2)
        if ask_play_again() == False:
            break