from funciones import *

listaPartidos = []

menu='''
    1 - Añadir partido
    2 - Buscar el resultado de un partido
    3 - Eliminar partido
    4 - Listar nombre de los equipos
    5 - Estadística de un equipo
    6 - Salir
    '''

opcion = 0

while opcion !=6:
    print(menu)
    opcion = int(input("Introduce una opción: "))

    if opcion==1:
        partidoParaAñadir = añadirPartido()
        listaPartidos.append(partidoParaAñadir)
        print(listaPartidos)

    elif opcion==2:
        busquedaPartido = buscaPartido(listaPartidos)
        print(busquedaPartido)

    elif opcion==3:
        eliminaPartido(listaPartidos)
        print(listaPartidos)