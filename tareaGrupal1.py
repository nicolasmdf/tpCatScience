'''

2) Función para ordenar de forma ascendente el vector de n elementos enteros
3) Función para buscar la moda
4) Función para buscar la media
5) Función para buscar la mediana
6) Función para conocer el rango del vector
7) Función para sumar 2 vectores
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

def cargarVector(): #devuelve un vector cargado por el usuario
    vector = []
    print("Ingrese un numero para agregar al vector, o presione x para salir")
    while True:
        n = input()
        if n == "x":
            break
        vector.append(int(n))
    return vector
