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
        listaEquipos.append(partido["equipoLocal"])
        listaEquipos.append(partido["equipoVisitante"])
    print(listaEquipos)
    

def estadisticaEquipo(listaPartidos):
    listaEquipos = []
    equipo = input("Introduzca el nombre del equipo: ")
    for partido in listaPartidos:
        partido()
