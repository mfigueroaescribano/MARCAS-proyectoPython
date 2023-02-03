from funciones import *

listaPartidos = []

menu='''
    1 - Añadir partido
    2 - Buscar el resultado de un partido
    3 - Eliminar partido
    4 - Listar nombre de los equipos
    5 - Estadística de un equipo
    6 - Muestra los datos
    7 - Salir
    '''

opcion = 0

while opcion !=7:
    print(menu)
    opcion = int(input("Introduce una opción: "))

    if opcion==1:
        partidoParaAñadir = añadirPartido()
        listaPartidos.append(partidoParaAñadir)

    elif opcion==2:
        busquedaPartido = buscaPartido(listaPartidos)
        print(busquedaPartido)

    elif opcion==3:
        eliminaPartido(listaPartidos)

    elif opcion==4:
        listaEquipos(listaPartidos)

    elif opcion==6:
        print(listaPartidos)

    else:
        print("Opción no valida, introduzca otra")
        
print("Gracias por usar el programa. ¡Adios!")