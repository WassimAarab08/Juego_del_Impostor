from Funciones_Juego import controlador_juego
if __name__ == "__main__":
    while True:
        controlador_juego()
        opcion = input("¿Queréis jugar otra partida? (S/N) => ").strip().upper()
        if opcion == "N":
            print("¡Gracias por jugar!.")
            break
        else:
            print("\n" * 40)