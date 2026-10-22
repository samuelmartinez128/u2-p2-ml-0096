import numpy as np
# Samuel Martinez NC 0096
# Ejemplos de Numpy Numerical Python
print("---- Espaciado Linealmente en array ---- 0096")
arre=np.linspace(start=0,stop=5,num=5)
print(arre)
print("---- Matriz identidad en 2D array ---- 0096")
matrix=np.eye(3)
print(matrix)
print("---- Genera numeros al azar(Aleatorios) en 2D array ---- 0096")
numale=np.random.random((3,4)) # Genera 12 numeros
print(numale)
print("genera 9 numeros aleatorios entre 0 y 1")
numale=np.random.random((3,3)) # Genera 9 numeros
print(numale)
# como generar 9 números aleatorios comprendidos entre 1 y 20 
# con Numpy en un arreglo de 3 por 3
print("genera 9 numeros aleatorios entre 1 y 21")
arre = np.random.randint(1, 21, size=9).reshape(3, 3)
print(arre)
print("Samuel Martinez NC 0096")