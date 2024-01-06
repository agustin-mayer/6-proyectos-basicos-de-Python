import random
import time #mide el tiempo del algoritmo

#la busqueda ingenua es la busqueda normal #target=objetivo=elemento buscado
def busqueda_ingenua(lista, target): #devuelve el indice donde esta el target
    for i in range(len(lista)): #range(len(lista)) -> 0, 1, 2, 3,...len(lista)-1
        if lista[i] == target:
            return i
    return -1

#Algoritmo recursivo. La lista tiene que estar ordenada.
#Si nadie asigna valor para los limites, se inicializan en None
def busqueda_binaria(lista,target,lim_inferior=None,lim_superior=None): 
    if lim_inferior is None:
        lim_inferior = 0
    if lim_superior is None:
        lim_superior = len(lista)-1 #Final de la lista
    
    if lim_superior < lim_inferior:
        return -1
    
    punto_medio = (lim_inferior + lim_superior) // 2 #division entera devuelve un entero

    if lista[punto_medio] == target:
        return punto_medio
    elif target < lista[punto_medio]:
        return busqueda_binaria(lista, target, lim_inferior, punto_medio-1)
    else: 
        return busqueda_binaria(lista, target, punto_medio + 1, lim_superior)
    
#Es una precaucion, solo se ejecuta el codigo si es main. Si alguien importa este modulo no se va a ejecutar la busqueda.
if __name__ == '__main__':
    
    #lista ordenada con 10000 numeros aleatorios
    tamano = 10000
    conjunto_inicial = set() #conjunto inicial vacio, los conjuntos no repiten valores
    
    while len(conjunto_inicial) < tamano:
        conjunto_inicial.add(random.randint(-3*tamano, 3*tamano))

    lista_ordenada = sorted(list(conjunto_inicial)) #convierte el conjunto en una lista, y sorted la ordena ascendente por defecto

    #Medir el tiempo de busqueda ingenua:
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_ingenua(lista_ordenada,objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda ingenua: {fin - inicio} segundos.")

    #Medir el tiempo de busqueda binaria:
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada,objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda binaria: {fin - inicio} segundos.")

