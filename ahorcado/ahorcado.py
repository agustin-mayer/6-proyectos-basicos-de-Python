import random
import string

from palabras import lista
from ahorcado_diagramas import vidas_diccionario_visual

def obtener_palabra_valida(listapalabras):
    palabra = random.choice(listapalabras)
    
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(listapalabras)
    
    return palabra.upper()

def ahorcado():

    print("====================================")
    print("       ¡Bienvenido/a al juego!      ")
    print("====================================")

    palabra = obtener_palabra_valida(lista)
    letras_por_adivinar = set(palabra) #convierte palabra en un conjunto: permite guardar elementos sin repetidos
    letras_ingresadas = set() #vacio, no {} porque esto crea un diccionario
    abecedario = set(string.ascii_uppercase) #sin Ñ

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_ingresadas)}") #une las letras usando espacios entre medio
        
        #Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_ingresadas else '_' for letra in palabra] #List Comprehension: Forma de escribir la lsita en una sola linea bajo una condicion
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {palabra_lista}")

        letra_usuario = input("Escoge una letra: ").upper()

        #Si la letra escogida esta en el abecedario y no esta en el conjunto de letras que ya se han ingresado, se añade la letra al conjunto de letras ingresadas.
        if letra_usuario in abecedario - letras_ingresadas:
            letras_ingresadas.add(letra_usuario)
            
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1 # esto es vidas = vidas - 1
                print(f"\nTu letra ({letra_usuario}) no esta en la palabra")
        #Si la letra ya fue ingresada
        elif letra_usuario in letras_ingresadas:
            print("\nYa ingresaste esa letra. Proba con otra")
        else:
            print("\nEsa letra no es valida. Proba con otra.")
    #Cuando se adivinan todas las letras o se terminan las vidas
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Ahorcado!! Perdiste. La palabra era: {palabra}")
    else:
        print(f"Muy bieeen, la palabra era {palabra} :)")

    
ahorcado()
