'''







8) Función para cargar 4 vectores de n elementos en una matriz
9) Función para pasar las columnas de una matriz 4x3 a vectores independientes
10) Función para pasar las filas de una matriz 4x3 a vectores independientes

No se pueden usar funciones de otras librerias como Numpy.

2) Deben escribir el codigo como funciones de los algoritmos. Hacer un menú que permita:

      1) Cargar 2 vectores.

       2) Sumar 2 vectores

      3) Multiplicar de forma escalar los 2 vectores. 

     4) salir 
'''

# 1) Función para cargar un vector de n elementos enteros.
def cargarVector(): 
    vector = []
    print("Ingrese un numero para agregar al vector, o presione x para salir")
    while True:
        n = input()
        if n == "x":
            break
        vector.append(int(n))
    return vector

# 2) Función para ordenar de forma ascendente el vector de n elementos enteros
def ordenarVector(vector):
    # con Bubble sort
    n = len(vector)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if vector[j] > vector[j + 1]:
                vector[j], vector[j + 1] = vector[j + 1], vector[j]
    return vector

# 3) Función para buscar la moda
def buscarModa(vector):
    frecuencias = {}
    for numero in vector:
        if numero not in frecuencias:
            frecuencias[numero] = 1
        else:
            frecuencias[numero] += 1

    mayor = 0
    for cantidad in frecuencias.values():
        if cantidad > mayor:
            mayor = cantidad

    modas = []
    for numero in frecuencias:
        if frecuencias[numero] == mayor:
            modas.append(numero)

    # Si solo hay una moda, devolver el número directamente
    if len(modas) == 1:
        return modas[0]
    else:
        return modas
    
# 4) Función para buscar la media
def buscarMedia(vector):
    i = 0
    for n in vector:
        i = i + n
    return i / len(vector)

# 5) Función para buscar la mediana
def buscarMediana(vector):
    ordenarVector(vector)
    n = len(vector)
    if n % 2 == 0:
        medio1 = vector[n // 2 - 1]
        medio2 = vector[n // 2]
        return (medio1 + medio2) / 2
    else:
        return vector[n // 2]
    
# 6) Función para conocer el rango del vector
def buscarRango(vector):
    ordenarVector(vector)
    n = len(vector)
    return vector[n-1] - vector[0]
# 7) Función para sumar 2 vectores
def sumarVectores(v1, v2):
    longitud = min(len(v1), len(v2))
    vectorSuma = []
    for i in range(longitud):
        vectorSuma.append(v1[i] + v2[i])
    # Si los vectores son de diferente tamaño, agrega los elementos que faltan
    if len(v1) > longitud:
        vectorSuma.extend(v1[longitud:])
    elif len(v2) > longitud:
        vectorSuma.extend(v2[longitud:])
    return vectorSuma