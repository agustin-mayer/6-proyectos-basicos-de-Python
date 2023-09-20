import random # necesito usar el modulo random


def adivinaElNumero(x): # def crea la funcion "adivinaElNumero"
                        # x = limite superior del intervalo valido de valores
    print("")
    print("  Bienvenido al juego  ")
    print("")
    print("Tu objetivo es adivinar el numero generado por la computadora.")
    print("")

    numeroAleatorio = random.randint(1,x) # aleatorio 1 =< N <= x 
    
    prediccion = 0 # inicializo la variable

    while prediccion != numeroAleatorio :
        # input devuelve siempre una cadena de caracteres, asique convierto con int
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: ")) 

        if prediccion < numeroAleatorio:
            print("Intenta otra vez. El que elegiste es muy chico")
        elif prediccion > numeroAleatorio:
            print("Intenta otra vez. Este numero es muy grande")
    
    print("Felicitaciones! Adivinaste el numero.") # ya estoy fuera del while
    # La guia de estilos de Python recomienda 2 lineas en blanco entre una funcion y cualquier otro elemento

adivinaElNumero(10)


