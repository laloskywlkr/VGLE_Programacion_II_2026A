#O(1) — Tiempo constante
def cr7_delantero():
    real_madrid_2017 = {
        "star": "Cristiano Ronaldo",
        "capitan": "Sergio Ramos"
    }

    return real_madrid_2017["star"] == "Cristiano Ronaldo"
#O(1) — Tiempo constante
def low_vol(vol_i):
    c_ajustes = 0

    while vol_i > 1:
        vol_i //= 2
        c_ajustes += 1

    return c_ajustes
#O(1) — Tiempo constante
def season_goals(match_goals):
    sum_g = 0

    for goals in match_goals:
        sum_g += goals

    return sum_g
#O(1) — Tiempo constante
def buscar_jugador_binario(squad_ordenada, name):
    left = 0
    right = len(squad_ordenada) - 1
    
    while left <= right:
        centro = (left + right) // 2
        
        if squad_ordenada[centro] == name:
            return True
        elif squad_ordenada[centro] < name:
            left = centro + 1
        else:
            right = centro - 1
    
    return False
#O(1) — Tiempo constante
def comparar_popularidad(lista_canciones):
    for i in range(len(lista_canciones)):
        for j in range(len(lista_canciones)):
            if lista_canciones[i]["streams"] > lista_canciones[j]["streams"]:
                pass
#O(1) — Tiempo constante
def combinaciones_penales(num_jugadores):
    total = 1

    for jugador in range(num_jugadores):
        total *= 2

    return total
#O(1) — Tiempo constante
def rutas_posibles(numero_planetas):
    total_rutas = 1

    for planeta in range(1, numero_planetas + 1):
        total_rutas *= planeta

    return total_rutas