import random 

intentos = 0

print("¡JUEGO DE ADIVINAR EL NÚMERO ALEATORIO!")

nombre = input("¿Cuál es tu nombre?\n")
x = random.randint(1,20) 

print("Hola " + nombre + ", Bienvenido a mi primer juego! Consiste en adivinar el número elegido al azar. Tenés 4 (cuatro) intentos! Suerte :)")

while intentos < 4:
    intentos = intentos + 1
    numero = input("Elegí un número del 1 al 20\n")
    numero = int(numero)

    if numero < x:
        print("Tu numero es más bajo, probá con otro.")
    if numero > x:
        print("Tu número es más alto, probá con otro.")
    if numero == x:
        print("Adivinaste el número")
        
    else:
        print("Perdiste el juego :(((")
    
    
    