from funciones import *

listaPartidos = []

menu='''
    1 - Leer fichero
    2 - Añadir partido
    3 - Buscar el resultado de un partido
    4 - Eliminar partido
    5 - Listar nombre de los equipos
    6 - Estadística de un equipo
    7 - Muestra los datos
    8 - Salir
    '''

opcion = 0

while opcion !=8:
    print(menu)
    opcion = int(input("Introduce una opción: "))

    if opcion==1:
        with open("ProyectoPython/data/ligabaloncesto.txt","r") as fichero:
            for linea in fichero:
                partido = {}
                partido["fecha"] = linea.split(",")[0]
                partido["equipoLocal"] = linea.split(",")[1]
                partido["equipoVisitante"] = linea.split(",")[2]
                partido["resultadoLocal"] = int(linea.split(",")[3])
                partido["resultadoVisitante"] = int(linea.split(",")[4].strip("\n)"))
                listaPartidos.append(partido)

    elif opcion==2:
        partidoParaAñadir = añadirPartido()
        listaPartidos.append(partidoParaAñadir)

    elif opcion==3:
        busquedaPartido = buscaPartido(listaPartidos)
        print(busquedaPartido)

    elif opcion==4:
        eliminaPartido(listaPartidos)

    elif opcion==5:
        listaEquipos(listaPartidos)

    elif opcion==6:
        estadisticaEquipo(listaPartidos)

    elif opcion==7:
        for partido in listaPartidos:
            print(partido)

    else:
        print("Opción no valida, introduzca otra")
        
print("Gracias por usar el programa. ¡Adios!")