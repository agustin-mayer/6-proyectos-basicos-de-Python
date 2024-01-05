import random

def adivinaElNumeroComputadora(x):

    print("====================================")
    print("       ¡Bienvenido/a al juego!      ")
    print(f" Selecciona un numero entre 1 y {x} ")
    print("====================================")

    limite_inferior = 1 # [1,x]
    limite_superior = x
    
    respuesta = ""

    while respuesta != "c":
        #Generar una prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior,limite_superior)
        else:
            prediccion = limite_inferior # Tambien podria ser el superior

        #Obtener una respuesta del usuario.!ALT+Z para que todo el texto entre
        respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta, ingresa A. Si es muy baja ingresa B. Si es correcta ingresa C: ").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"La computadura adivino tu numero correctamente!")


adivinaElNumeroComputadora(10)