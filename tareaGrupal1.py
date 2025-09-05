'''
1) Codear las 10 funciones
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

# 8) Función para cargar 4 vectores de n elementos en una matriz
def cargarMatriz(v1,v2,v3,v4):
    mat = [v1,v2,v3,v4]
    return mat

# 9) Función para pasar las columnas de una matriz 4x3 a vectores independientes
def colsAVectores(mat):
    v1 = [mat[0][0], mat[1][0], mat[2][0], mat[3][0]]
    v2 = [mat[0][1], mat[1][1], mat[2][1], mat[3][1]]
    v3 = [mat[0][2], mat[1][2], mat[2][2], mat[3][2]]
    return v1, v2, v3

# 10) Función para pasar las filas de una matriz 4x3 a vectores independientes
def filasAVectores(mat):
    v1 = mat[0]
    v2 = mat[1]
    v3 = mat[2]
    v4 = mat[3]
    return v1, v2, v3, v4

def main():
    vector1, vector2 = []
    print('Bienvenido, elija 1 para cargar vectores, 2 para sumarlos o 3 para multiplicarlos. Presione x para salir.')
    while True:
        n = input()
        if n == "x":
            break
    if n == 1 and len(vector1) == 0:
        vector1 = cargarVector()
    elif n == 1 and len(vector2) == 0:
        vector2 = cargarVector()
    elif len(vector1) != 0 and len(vector2) != 0:
        print('Ambos vectores han sido cargados')
        