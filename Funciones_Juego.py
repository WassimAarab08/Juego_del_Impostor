jugadores_dicc = {}
jugadores_respuestas = {}
diccionario_palabras = {}
palabra_secreta = ""
numero_rondas = 3
diccionario_votos = {}


# Funcion encargada de solicitar el numero de participantes y sus nombres. Cuenta con validacion de entradas
def solicitar_datos():
    print("====================== BIENVENIDO AL JUEGO DEL IMPOSTOR ====================== \n")
    numero_participantes = validar_datos("FN_solicitar_datos")

    for i in range(numero_participantes):
        nombre_jugador = input(f"Jugador número {i + 1}, introduzca su nombre por favor => ")

        while True:
            if nombre_jugador in jugadores_dicc:
                nombre_jugador = input("Ese nombre ya está en uso, pruebe con otro => ")
            else:
                break

        jugadores_dicc[nombre_jugador] = "INOCENTE"
        jugadores_respuestas[nombre_jugador] = []
        diccionario_votos[nombre_jugador] = 0

# Funcion que es llamada por diferentes funciones para comprobar algún tipo de entrada
def validar_datos(tipo_a_validar):
    match tipo_a_validar:

        case "FN_solicitar_datos":
            numero_participantes = 0
            while numero_participantes < 3:
                try:
                    numero_participantes = int(input("Introduzca el número de participantes (mínimo 3) => "))
                except ValueError:
                    print("Entrada no válida, ya que no es un número.")
            return numero_participantes

        case _:
            return None



