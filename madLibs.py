# # Concatenar cadenas de caracteres.

# organizacion = "agustin"

# #forma clean
# print("Hola me llamo " + organizacion)

# #otra forma
# print("Hola me llamo {}".format(organizacion))

# #la recomendada y mas optimizada: usando f-string
# print(f"Hola me llamo {organizacion}")

#Mad Libs (Historias Locas)

adjetivo = input("Adjetivo: ") #permite pedirle al usuario un valor. Conviene dejar espacio para separar la barrita
verbo = input("Verbo: ")
sustantivo = input("Sustantivo: ")

madlib = f"Ayer estaba {verbo} cuando escuche un {sustantivo}, por lo que deje de hacerlo. Despues estaba {adjetivo} por lo que segui"

print (madlib)