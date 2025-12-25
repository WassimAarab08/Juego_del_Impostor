import random

lista_jugadores = []
nombre_impostor=""
jugadores_respuestas = {}
diccionario_palabras = {
    "Playa": "Bañador",
    "Leon": "Tigre",
    "Avion": "Helicoptero",
    "Invierno": "Nieve",
    "Medico": "Enfermero",
    "Desierto": "Oasis",
    "Reloj": "Cronometro",
    "Oro": "Plata",
    "Libro": "Cuaderno",
    "Bosque": "Selva",
    "Coche": "Motocicleta",
    "Luna": "Estrella",
    "Pan": "Arroz",
    "Herramienta": "Maquinaria",
    "Bicicleta": "Patinete",
    "Montaña": "Volcan",
    "Telefono": "Ordenador",
    "Zapato": "Sandalia",
    "Arquitecto": "Ingeniero",
    "Carpintero": "Albañil",
    "Martillo": "Destornillador",
    "Arbol": "Planta",
    "Lluvia": "Tormenta",
    "Puente": "Tunel",
    "Miel": "Datiles"
}
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
            if nombre_jugador in lista_jugadores:
                nombre_jugador = input("Ese nombre ya está en uso, pruebe con otro => ")
            else:
                break

        lista_jugadores.append(nombre_jugador)
        jugadores_respuestas[nombre_jugador] = []
        diccionario_votos[nombre_jugador] = 0


# Función encargada de selecionar el impostor aleatoriamente y la palabra secreta

def seleccion_random():
    global nombre_impostor, palabra_secreta
    nombre_impostor = random.choice(lista_jugadores)
    lista_palabras_secretas = list(diccionario_palabras.keys())
    palabra_secreta= random.choice(lista_palabras_secretas)


# Función encargada de mostrar la palabra a cada participante

def mostrar_palabra():

    for jugador in lista_jugadores:

        input(f"Turno de {jugador} pulse cualquiere tecla para ver la palabra secreta y su rol")
        if jugador == nombre_impostor:
            print(f"Role: 🔴 IMPOSTOR 🔴\n Pista: {diccionario_palabras[palabra_secreta]}")
            input("Pulsa cualquiere tecla para pasarle al siguiente participante y ocultar tu rol y palabra")
            print("\n"*22)
        else:
            print(f"Role: Inocente \n Palabra: 🔒{palabra_secreta}🔒")
            input("Pulsa cualquiere tecla para pasarle al siguiente participante y ocultar tu rol y palabra")
            print("\n" * 22)
























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



