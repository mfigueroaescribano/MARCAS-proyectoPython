# AÑADIR PARTIDO
def añadirPartido():

    fecha = input("Introduce la fecha del partido, en el formato DD/MM/AAAA: ")
    equipoLocal = input("Introduce el nombre del equipo local: ")
    equipoVisitante = input("Introduce el nombre del equipo visitante: ")
    resultadoLocal = int(input("Introduce el resultado del equipo local: "))
    resultadoVisitante = int(input("Introduce el resultado del equipo visitante: "))
    
    partido = {
        'fecha' : fecha,
        'equipoLocal' : equipoLocal,
        'equipoVisitante' : equipoVisitante,
        'resultadoLocal' : resultadoLocal,
        'resultadoVisitante' : resultadoVisitante
    }
    return(partido)

# BUSCAR PARTIDO
def buscaPartido(listaPartidos):
    fechaPartidoBusqueda = input("Introduzca la fecha del partido: ")
    equipoLocalBusqueda = input("Introduzca el equipo local: ")
    for partido in listaPartidos:
        if partido["equipoLocal"] == equipoLocalBusqueda and partido["fecha"] == fechaPartidoBusqueda:
            print(partido["equipoLocal"], partido["resultadoLocal"], "-" ,partido["resultadoVisitante"], partido["equipoVisitante"])

# ELIMINAR PARTIDO
def eliminaPartido(listaPartidos):
    equipoLocalBusqueda = input("Introduzca el equipo local: ")
    equipoVisitanteBusqueda = input("Introduzca el equipo visitante: ")
    for partido in listaPartidos:
        if partido["equipoLocal"] == equipoLocalBusqueda and partido["equipoVisitante"] == equipoVisitanteBusqueda:
            listaPartidos.remove(partido)

# LISTA DE EQUIPOS
def listaEquipos(listaPartidos):
    listaEquipos = []
    for partido in listaPartidos:
        if partido["equipoLocal"] not in listaEquipos:
            listaEquipos.append(partido["equipoLocal"])
        if partido["equipoVisitante"] not in listaEquipos:
            listaEquipos.append(partido["equipoVisitante"])
    print(listaEquipos)
    

def estadisticaEquipo(listaPartidos):
    equipo = input("Introduzca el nombre del equipo: ")
    puntosEquipo = 0
    partidosGanados = 0
    partidosPerdidos = 0
    # No puede haber empate
    for partido in listaPartidos:
        if partido["equipoLocal"] == equipo:
            puntosEquipo += partido["resultadoLocal"]
            if partido["resultadoLocal"] > partido["resultadoVisitante"]:
                partidosGanados =+ 1
            else:
                partidosPerdidos =+ 1
        if partido["equipoVisitante"] == equipo:
            puntosEquipo += partido["resultadoVisitante"]
            if partido["resultadoLocal"] > partido["resultadoVisitante"]:
                partidosPerdidos =+ 1
            else:
                partidosGanados =+ 1
    print(f"{equipo} ha anotado {puntosEquipo} puntos")
    print(f"{equipo} ha ganado {partidosGanados} partidos")
    print(f"{equipo} ha perdido {partidosPerdidos} partidos")