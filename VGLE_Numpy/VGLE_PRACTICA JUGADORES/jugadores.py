import numpy as np

#Leer csv
#con esta función abre el archivo csv
datosJugadores=np.genfromtxt (
    "jugadores_futbol.csv",
    delimiter=",",
    dtype=None,
    encoding="utf-8",#Subclasificación de caracteres
    names=True
)
print(datosJugadores)

#Obtener los 5 mejores jugadores
jugadoresOrdenados = np.sort( #Se ordenan primero
    datosJugadores,
    order="Goles"
    )
top5=jugadoresOrdenados[-5:] 
print(f"Top 5 de goleadores: \n {top5}")

promedioEdad=np.mean(datosJugadores["Edad"])
print(f"Promedio de edad: {promedioEdad}")

#10 Jugadores más caros
OrdenvalorMercado= np.sort( #Se ordenan primero
    datosJugadores,
    order="ValorMercado"
    )
JugadoresCaros=OrdenvalorMercado[-10:]
print(f"Jugadores más caros: {JugadoresCaros}")

np.savetxt(
    "JugadoresCaros.csv",
    JugadoresCaros,
    delimiter=",",
    fmt="%s",
    header="ID, JUGADOR, EQUIPO, POSICION, EDAD, PARTIDOS, GOLES, ASISTENCIAS, VALOR MERCADO"
)
#Ejercicio:
#Total de todos los goles
suma=np.sum(datosJugadores["Goles"])
print(f"Total de goles: {suma}")
#Promedio de los goles
promedio=np.mean(datosJugadores["Goles"])
print(promedio)
#Máxima cantidad de goles
Maxgoles=np.max(datosJugadores["Goles"])
print(Maxgoles)