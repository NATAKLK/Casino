import os
# ...existing code...
# Colores ANSI para la terminal 
C_RESET = '\033[0m'

# Estilos
C_BOLD = '\033[1m'
C_DIM = '\033[2m'
C_ITALIC = '\033[3m'
C_UNDERLINE = '\033[4m'
C_BLINK = '\033[5m'
C_REVERSE = '\033[7m'
C_HIDDEN = '\033[8m'

# Colores foreground (estándar)
C_BLACK = '\033[30m'
C_ROJO = '\033[31m'       # ya usado en el código
C_VERDE = '\033[32m'      # ya usado en el código
C_AMARILLO = '\033[33m'   # ya usado en el código
C_AZUL = '\033[34m'
C_MAGENTA = '\033[35m'
C_CYAN = '\033[36m'       # ya usado en el código
C_BLANCO = '\033[37m'
# Colores foreground brillantes
C_BLACK_BRIGHT = '\033[90m'
C_ROJO_BRIGHT = '\033[91m'
C_VERDE_BRIGHT = '\033[92m'
C_AMARILLO_BRIGHT = '\033[93m'
C_AZUL_BRIGHT = '\033[94m'
C_MAGENTA_BRIGHT = '\033[95m'
C_CYAN_BRIGHT = '\033[96m'
C_BLANCO_BRIGHT = '\033[97m'

# Backgrounds
BG_BLACK = '\033[40m'
BG_ROJO = '\033[41m'
BG_VERDE = '\033[42m'
BG_AMARILLO = '\033[43m'
BG_AZUL = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_BLANCO = '\033[47m'
# Backgrounds brillantes
BG_BLACK_BRIGHT = '\033[100m'
BG_ROJO_BRIGHT = '\033[101m'
BG_VERDE_BRIGHT = '\033[102m'
BG_AMARILLO_BRIGHT = '\033[103m'
BG_AZUL_BRIGHT = '\033[104m'
BG_MAGENTA_BRIGHT = '\033[105m'
BG_CYAN_BRIGHT = '\033[106m'
BG_BLANCO_BRIGHT = '\033[107m'

# Mapa completo (útil para listar o usar por nombre)
ALL_ANSI_COLORS = {
    "RESET": C_RESET,
    "BOLD": C_BOLD, "DIM": C_DIM, "ITALIC": C_ITALIC, "UNDERLINE": C_UNDERLINE,
    "BLINK": C_BLINK, "REVERSE": C_REVERSE, "HIDDEN": C_HIDDEN,
    "BLACK": C_BLACK, "ROJO": C_ROJO, "VERDE": C_VERDE, "AMARILLO": C_AMARILLO,
    "AZUL": C_AZUL, "MAGENTA": C_MAGENTA, "CYAN": C_CYAN, "BLANCO": C_BLANCO,
    "BLACK_BRIGHT": C_BLACK_BRIGHT, "ROJO_BRIGHT": C_ROJO_BRIGHT, "VERDE_BRIGHT": C_VERDE_BRIGHT,
    "AMARILLO_BRIGHT": C_AMARILLO_BRIGHT, "AZUL_BRIGHT": C_AZUL_BRIGHT, "MAGENTA_BRIGHT": C_MAGENTA_BRIGHT,
    "CYAN_BRIGHT": C_CYAN_BRIGHT, "BLANCO_BRIGHT": C_BLANCO_BRIGHT,
    "BG_BLACK": BG_BLACK, "BG_ROJO": BG_ROJO, "BG_VERDE": BG_VERDE, "BG_AMARILLO": BG_AMARILLO,
    "BG_AZUL": BG_AZUL, "BG_MAGENTA": BG_MAGENTA, "BG_CYAN": BG_CYAN, "BG_BLANCO": BG_BLANCO,
    "BG_BLACK_BRIGHT": BG_BLACK_BRIGHT, "BG_ROJO_BRIGHT": BG_ROJO_BRIGHT, "BG_VERDE_BRIGHT": BG_VERDE_BRIGHT,
    "BG_AMARILLO_BRIGHT": BG_AMARILLO_BRIGHT, "BG_AZUL_BRIGHT": BG_AZUL_BRIGHT, "BG_MAGENTA_BRIGHT": BG_MAGENTA_BRIGHT,
    "BG_CYAN_BRIGHT": BG_CYAN_BRIGHT, "BG_BLANCO_BRIGHT": BG_BLANCO_BRIGHT,
}
    
def listar_colores():
    """Imprime una muestra de los colores disponibles (para terminales que soporten ANSI)."""
    for nombre, codigo in ALL_ANSI_COLORS.items():
        # evitar imprimir RESET solo como muestra
        if nombre == "RESET":
            continue
        print(f"{codigo}{nombre}{C_RESET}", end="  ")
    print()
# ...existing code...