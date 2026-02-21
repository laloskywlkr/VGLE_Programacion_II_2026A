from datetime import datetime

inicio = datetime.now()
print("Inicio:", inicio)

filas = 8
columnas = 8

tablero = []
valor = 1

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(valor)
        valor *= 2
    tablero.append(fila)

print("\nTABLERO:\n")

for i in range(filas):
    for j in range(columnas):
        print(tablero[i][j], end=" ")
    print()

total = 0
for i in range(filas):
    for j in range(columnas):
        total += tablero[i][j]

print("\nTotal:", total)

fin = datetime.now()
print("Fin:", fin)

duracion = fin - inicio
print("Tiempo de ejecución:", duracion)