HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ======="""
]
#
WORD_LIST_ES_PROGRAM = [
    "variable", "bucle", "funcion", "clase", "objeto", "metodo",
    "lista", "diccionario", "archivo", "programa", "cadena",
    "entero", "decimal", "booleano", "verdadero", "falso",
    "condicion", "while", "for", "if", "else", "menu",
    "pantalla", "teclado", "raton", "impresora", "memoria",
    "disco", "carpeta", "archivo", "red", "internet",
    "web", "correo", "usuario", "contraseña", "base",
    "datos", "tabla", "columna", "fila", "registro",
    "conexion", "servidor", "cliente", "ventana", "boton",
    "imagen", "audio", "video", "juego", "nivel"
]
WORD_LIST_EN_PROGRAM = [
    "variable", "loop", "function", "class", "object", "method",
    "list", "dictionary", "file", "program", "string", 
    "integer", "float", "boolean", "true", "false",
    "condition", "while", "for", "if", "else", "menu",
    "screen", "keyboard", "mouse", "printer", "memory",
    "disk", "folder", "file", "network", "internet",
    "web", "email", "user", "password", "database",
    "data", "table", "column", "row", "record",
    "connection", "server", "client", "window", "button",
    "image", "audio", "video", "game", "level"
]
TECH_WORDS_EN = [
    "ai","machine learning","cloud","virtualization","container",
    "docker","kubernetes","iot","blockchain","cybersecurity",
    "encryption","api","microservices","edge","big data",
    "analytics","virtual reality","augmented reality","devops","serverless"
]

TECH_WORDS_ES = [
    "ia","aprendizaje","nube","virtualizacion","contenedor",
    "docker","kubernetes","iot","blockchain","ciberseguridad",
    "encriptacion","api","microservicios","edge","big data",
    "analitica","realidad virtual","realidad aumentada","devops","sin servidor"
]

# Paises y capitales (tuplas: (pais, capital)) — inglés y español
COUNTRIES_CAPITALS_EN = [
    ("Spain","Madrid"),("France","Paris"),("Germany","Berlin"),("Italy","Rome"),
    ("United Kingdom","London"),("United States","Washington"),("Mexico","Mexico City"),
    ("Argentina","Buenos Aires"),("Brazil","Brasilia"),("Japan","Tokyo"),
    ("China","Beijing"),("Russia","Moscow"),("India","New Delhi"),
    ("Canada","Ottawa"),("Australia","Canberra")
]

COUNTRIES_CAPITALS_ES = [
    ("España","Madrid"),("Francia","París"),("Alemania","Berlín"),("Italia","Roma"),
    ("Reino Unido","Londres"),("Estados Unidos","Washington"),("México","Ciudad de México"),
    ("Argentina","Buenos Aires"),("Brasil","Brasilia"),("Japón","Tokio"),
    ("China","Pekín"),("Rusia","Moscú"),("India","Nueva Delhi"),
    ("Canadá","Ottawa"),("Australia","Canberra")
]

# Animales (inglés / español)
ANIMALS_EN = [
    "dog","cat","horse","cow","pig","sheep","goat","lion","tiger","bear",
    "elephant","rabbit","fox","wolf","deer","monkey","bird","fish","whale","dolphin"
]

ANIMALS_ES = [
    "perro","gato","caballo","vaca","cerdo","oveja","cabra","leon","tigre","oso",
    "elefante","conejo","zorro","lobo","ciervo","mono","pajaro","pez","ballena","delfin",""
]

# Marcas de coches, motos y marcas generales
CAR_BRANDS = [
    "Subaru","Mazda","Mitsubishi","Chrysler","Jeep","Cadillac","Infiniti",
    "Acura","Genesis","Fiat","Mini","Seat","Skoda","Alfa Romeo","MG",
    "Geely","BYD","Koenigsegg","McLaren","Bentley","Rolls-Royce",
    "Aston Martin","Bugatti","Lamborghini","Ferrari","Pagani","Lotus"
]

MOTORCYCLE_BRANDS = [
    "Aprilia","Husqvarna","MV Agusta","Royal Enfield","GasGas",
    "Bimota","Benelli","Cagiva","Derbi","Guzzi","KTM","Ducati",
    "Yamaha","Suzuki","Kawasaki","Honda","Triumph","Harley"
    ]

GENERAL_BRANDS = [
    "Starbucks","Netflix","Uber","Airbnb","Spotify","DHL","FedEx",
    "Bosch","Siemens","Panasonic","Philips","Cartier","Rolex","Loreal",
    "Dior","H&M","Zara","Uniqlo","LVMH","Puma","Under Armour",
    "Canon","Nikon","GoPro","Xiaomi","Oppo","Vivo","OnePlus","Lenovo",
    "Asus","Acer","Razer","MSI"
]

ALL_BRANDS = CAR_BRANDS + MOTORCYCLE_BRANDS + GENERAL_BRANDS