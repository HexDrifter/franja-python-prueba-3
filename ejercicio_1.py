# Escribir un programa que escriba 20 numeros aleatorios
# entre 100 y 1000 en un archivo llamado numeros_prueba.txt.
# Luego debe leer desde el archivo esos números y agregarlos
# a una lista, modifique o cree una nueva lista que contenga
# solo los numeros impares. Finalmente con numpy determinar
# la dimensión de la lista. Imprimir por consola la lista
# final y su dimensión.
import numpy as np
import random as rnd

def main():
    numeros = []
    impares = []
    for i in range (20):
        numeros.append(rnd.randint(100,1000))

    with open('./numeros_prueba.txt', 'w', encoding="utf-8") as file:
        for num in numeros:
            file.write(str(num))
            file.write("\n")
    
    with open('./numeros_prueba.txt', 'r') as file:
        for row in file:
            if((int(row) %2)==1):
                impares.append(int(row))

    print("Impares:", impares)
    npImpar = np.array(impares)
    print("Dimension:", npImpar.ndim)
    print("Ejecución finalizada")


if __name__ == '__main__':
    main()