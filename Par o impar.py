'''
Par o impar
Lo primero que vamos a realizar es dar la bienvenida preguntando un número entre 1 y 1000

Cuando el usuario proporciona el número, comprobaremos si es par o impar y después imprimimos el mensaje con el resultado.

Ejemplo:

Mensaje que se muestra: ¿En qué número estás pensando?
Entrada: 25
Salida: ¡Es un número impar! ¿Puedes añadir otro?
'''

num_user = int(input("Escribe un número entre 1 y 1000: "))

if num_user % 2 == 0:
    print(num_user, "¡Es un número par!")

else:
    print(num_user, "¡Es un número impar!")