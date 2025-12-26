import random

lista_jugadores = []
nombre_impostor=""
diccionario_respuestas = {}
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
        nombre_jugador = input(f"Jugador número {i + 1}, introduzca su nombre por favor => ").strip().capitalize()

        while True:
            if nombre_jugador in lista_jugadores:
                nombre_jugador = input("Ese nombre ya está en uso, pruebe con otro => ").strip().capitalize()
            else:
                break

        lista_jugadores.append(nombre_jugador)
        diccionario_respuestas[nombre_jugador] = []
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


# Función encargada de gestionar las rondas

def generador_rondas():
    for i in range(numero_rondas):
        print(f"============= Ronda {i+1} =============")
        for jugador in lista_jugadores:
            respuesta= validar_datos("FN_generador_ronda",jugador)
            diccionario_respuestas[jugador].append(respuesta)


# Función encargada de gestionar las votaciones

def gestion_votacion():
    print("============= HORA DE VOTAR =============")

    for jugadores_respuestas in lista_jugadores:
        print(f"🔵 Respuestas de {jugadores_respuestas} 🔵")

        for respuesta in diccionario_respuestas[jugadores_respuestas]:
            print(f"- {respuesta}")


    for jugador in lista_jugadores:
        voto_jugador = validar_datos("FN_gestion_votacion",jugador)
        diccionario_votos[voto_jugador]=diccionario_votos.get(voto_jugador,0)+1



















# Funcion que es llamada por diferentes funciones para comprobar algún tipo de entrada
def validar_datos(tipo_a_validar,jugador="None"):
    match tipo_a_validar:

        case "FN_solicitar_datos":
            numero_participantes = 0
            while numero_participantes < 3:
                try:
                    numero_participantes = int(input("Introduzca el número de participantes (mínimo 3) => "))
                except ValueError:
                    print("Entrada no válida, ya que no es un número.")
            return numero_participantes

        case "FN_generador_ronda":
                jugador_respuesta = input(f"\n{jugador.upper()} escribe tu respuesta para esta ronda => ")
                while len(jugador_respuesta)<2:
                    jugador_respuesta = input(f"\n{jugador.upper()} escribe tu respuesta para esta ronda debe ser almenos de 2 letras => ")

                return jugador_respuesta
        case "FN_gestion_votacion":
              votacion = input(f"{jugador} escribe el nombre de la persona a la que votas => ").strip().capitalize()
              while votacion not in lista_jugadores:
                  print("============= Nombre invalido ============= ")
                  votacion= input(f"{jugador} escribe el nombre de la persona a la que votas => ").strip().capitalize()
              return votacion

        case _:
            return None



