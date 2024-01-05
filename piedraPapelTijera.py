import random

def jugar():
    usuario = input("Escoge una opcion: Piedra, papel o tijera:\n").lower()
    computadora = random.choice(['piedra','papel','tijera'])

    if (usuario == computadora):
        return 'Empate!'
    
    if ganoElJugador(usuario,computadora):
        return 'Ganaste!'
    
    return 'Perdiste!'


def ganoElJugador(usuario,computadora):
    if ((usuario == 'piedra' and computadora == 'tijera') or (usuario == 'tijera' and computadora == 'papel') or (usuario == 'papel' and computadora == 'piedra')):
        return True
    else:
        return False
        

print(jugar())