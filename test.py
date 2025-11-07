def eleccion():
    print("elige")
    choice = int(input())
    if choice == 1:
        print("elegiste 1")
    elif choice == 2:
        print("elegiste 2")
    elif choice == 3:
        print("elegiste 3")
    else:
        print("Elige del 1 al 3")
        eleccion()

eleccion()