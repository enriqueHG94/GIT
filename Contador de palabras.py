'''Contador de palabras
Preguntamos al usuario en que está pensando. Cuando se introduce la respuesta,
realizará el conteo de palabras en la sentencia e imprimimos en la salida el resultado.

Ejemplo:

Pregunta: ¿En qué estás pensando?
Entrada: Bien, hoy es el día en el que me voy a crear un desarrollador experto
Salida: ¡Muy bien, tu me has mostrado tu pensamiento en 15 palabras!
'''



user = input("¿Qué tal estás?: ")

result = len(user.split())

print("Genial, me has dicho como estás en " + str(result) + " palabras.")