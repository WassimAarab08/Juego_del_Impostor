import random

# Función encargada de solicitar el número de participantes y sus nombres
def solicitar_datos():
    lista_jugadores_temp = []
    diccionario_respuestas_temp = {}
    diccionario_votos_temp = {}
    print("====================== BIENVENIDO AL JUEGO DEL IMPOSTOR ====================== \n")
    numero_participantes = validar_datos("FN_solicitar_datos")

    for i in range(numero_participantes):
        nombre_jugador = input(f"Jugador número {i + 1}, introduzca su nombre, por favor => ").strip().capitalize()

        while True:
            if nombre_jugador in lista_jugadores_temp:
                nombre_jugador = input("Ese nombre ya está en uso, pruebe con otro => ").strip().capitalize()
            else:
                break

        lista_jugadores_temp.append(nombre_jugador)
        diccionario_respuestas_temp[nombre_jugador] = []
        diccionario_votos_temp[nombre_jugador] = 0
    print("\n" * 100)
    return lista_jugadores_temp, diccionario_respuestas_temp, diccionario_votos_temp


# Función encargada de seleccionar el impostor aleatoriamente y la palabra secreta
def seleccion_random(lista_jugadores, diccionario_palabras):
    nombre_impostor = random.choice(lista_jugadores)
    lista_palabras_secretas = list(diccionario_palabras.keys())
    palabra_secreta = random.choice(lista_palabras_secretas)
    return nombre_impostor, palabra_secreta


# Función encargada de mostrar la palabra a cada participante
def mostrar_palabra(lista_jugadores, nombre_impostor, diccionario_palabras, palabra_secreta):
    print("==================== HORA DE VER LA PALABRA Y EL ROL DE CADA UNO ====================")
    for jugador in lista_jugadores:

        input(f"Turno de {jugador}, pulse cualquier tecla para ver la palabra secreta y su rol => ")
        if jugador == nombre_impostor:
            print(f"Rol: 🔴 IMPOSTOR 🔴\nPista: {diccionario_palabras[palabra_secreta]}")
            input("Pulsa cualquier tecla para pasar al siguiente participante y ocultar tu rol y palabra => ")
            print("\n" * 100)
        else:
            print(f"Rol: Inocente \nPalabra: 🔒{palabra_secreta}🔒")
            input("Pulsa cualquier tecla para pasar al siguiente participante y ocultar tu rol y palabra => ")
            print("\n" * 100)


# Función encargada de gestionar las rondas
def generador_rondas(diccionario_respuestas, numero_rondas, lista_jugadores):

    resultado_temp=[]
    for i in range(numero_rondas):
        print(f"\n============= Ronda {i + 1} =============")
        for jugador in lista_jugadores:
            respuesta = validar_datos("FN_generador_ronda", jugador,resultado_temp)
            resultado_temp.append(respuesta)
            diccionario_respuestas[jugador].append(respuesta)


# Función encargada de gestionar las votaciones
def gestion_votacion(lista_jugadores, diccionario_respuestas, diccionario_votos):
    print("\n" * 100)
    print("============= HORA DE VOTAR =============")

    for jugadores_respuestas in lista_jugadores:
        print(f"🔵 Respuestas de {jugadores_respuestas} 🔵")

        for respuesta in diccionario_respuestas[jugadores_respuestas]:
            print(f"- {respuesta}")

    for jugador in lista_jugadores:
        voto_jugador = validar_datos("FN_gestion_votacion", jugador, lista_jugadores)
        diccionario_votos[voto_jugador] = diccionario_votos.get(voto_jugador, 0) + 1
    return diccionario_votos

# Función encargada de mostrar el resultado
def mostrar_resultado(diccionario_votos, nombre_impostor, palabra_secreta, diccionario_palabras):
    max_votos = max(diccionario_votos.values())
    lista_ganadores = [jugador for jugador, votos in diccionario_votos.items() if votos == max_votos]
    print("\n" * 3)
    print("=== Lista de votos de cada jugador ===")
    for jugador in diccionario_votos:
        print(f"{jugador}: {diccionario_votos[jugador]} ")

    print("\n" + "*" * 40)

    if len(lista_ganadores) > 1 and (nombre_impostor in lista_ganadores):
        print("EMPATE EN LA VOTACIÓN")
        print(f"El impostor era {nombre_impostor}")
        print(f"La palabra secreta era {palabra_secreta}")
        print(f"La pista era {diccionario_palabras[palabra_secreta]}")
    elif nombre_impostor not in lista_ganadores:
        print("GANA EL IMPOSTOR")
        print(f"El impostor era {nombre_impostor}")
        print(f"La palabra secreta era {palabra_secreta}")
        print(f"La pista era {diccionario_palabras[palabra_secreta]}")
    else:
        print("GANAN LOS INOCENTES")
        print(f"El impostor era {nombre_impostor}")
        print(f"La palabra secreta era {palabra_secreta}")
        print(f"La pista era {diccionario_palabras[palabra_secreta]}")

    print("*" * 40 + "\n")


# Función para validar las entradas
def validar_datos(tipo_a_validar, jugador="None", lista=None):
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
            while len(jugador_respuesta) < 2 or jugador_respuesta in lista:
                jugador_respuesta = input(
                    f"\n{jugador.upper()} escribe tu respuesta (⚠️Debe tener al menos 2 letras y no repetirse.⚠️) => ")

            return jugador_respuesta

        case "FN_gestion_votacion":
            votacion = input(f"{jugador}, escribe el nombre de la persona a la que votas => ").strip().capitalize()
            while (votacion not in lista) or votacion == jugador:
                print("Error Nombre inválido o intento de auto-voto.")
                votacion = input("Introduce un nombre válido => ").strip().capitalize()
            return votacion

        case _:
            return None


# --- INICIO DEL JUEGO ---

def controlador_juego():
    lista_jugadores, diccionario_respuestas, diccionario_votos = solicitar_datos()
    diccionario_palabras = {
        "Playa": "Bañador",
        "León": "Tigre",
        "Avión": "Helicóptero",
        "Invierno": "Nieve",
        "Médico": "Enfermero",
        "Desierto": "Oasis",
        "Reloj": "Cronómetro",
        "Oro": "Plata",
        "Libro": "Cuaderno",
        "Bosque": "Selva",
        "Coche": "Motocicleta",
        "Luna": "Estrella",
        "Pan": "Arroz",
        "Herramienta": "Maquinaria",
        "Bicicleta": "Patinete",
        "Montaña": "Volcán",
        "Teléfono": "Ordenador",
        "Zapato": "Sandalia",
        "Arquitecto": "Ingeniero",
        "Carpintero": "Albañil",
        "Martillo": "Destornillador",
        "Árbol": "Planta",
        "Lluvia": "Tormenta",
        "Puente": "Túnel",
        "Miel": "Dátiles"
    }
    numero_rondas = 3
    nombre_impostor, palabra_secreta = seleccion_random(lista_jugadores, diccionario_palabras)
    mostrar_palabra(lista_jugadores, nombre_impostor, diccionario_palabras, palabra_secreta)
    generador_rondas(diccionario_respuestas, numero_rondas, lista_jugadores)
    gestion_votacion(lista_jugadores, diccionario_respuestas, diccionario_votos)
    mostrar_resultado(diccionario_votos, nombre_impostor, palabra_secreta, diccionario_palabras)


