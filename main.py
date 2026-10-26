from procesamiento import (
    cargar_alumnos,
    mostrar_listado,
    mostrar_estadisticas,
    ordenar_por_promedio,
    buscar_alumno,
    analizar_nombre
)


nombres = []
notas_parcial_1 = []
notas_parcial_2 = []
promedios = []

opcion = 0

print("¡Bienvenida!")

while opcion != 7:
    #Mostramos las opciones del programa.
    print("****************************")
    print("1 - Cargar alumnos")
    print("2 - Mostrar listado")
    print("3 - Mostrar estadísticas")
    print("4 - Ver ranking")
    print("5 - Buscar alumno")
    print("6 - Juego con un nombre")
    print("7 - Salir")
    print("****************************")
    opcion = int(input("Seleccione una  opción: "))

    match opcion:
        case 1:
            nombres, notas_parcial_1, notas_parcial_2, promedios = cargar_alumnos()
            print("Carga finalizada.")

        case 2:
            if len(nombres) == 0:
                print("Primero debe cargar alumnos.")
            else:
                mostrar_listado(
                    nombres,
                    notas_parcial_1,
                    notas_parcial_2,
                    promedios
                )

        case 3:
            if len(nombres) == 0:
                print("Primero debe cargar alumnos.")
            else:
                mostrar_estadisticas(nombres, promedios)

        case 4:
            if len(nombres) == 0:
                print("Primero debe cargar alumnos.")
            else:
                ordenar_por_promedio(
                    nombres,
                    notas_parcial_1,
                    notas_parcial_2,
                    promedios
                )

        case 5:
            if len(nombres) == 0:
                print("Primero debe cargar alumnos.")
            else:
                buscar_alumno(
                    nombres,
                    notas_parcial_1,
                    notas_parcial_2,
                    promedios
                )

        case 6:
            analizar_nombre()

        case 7:
            print("Saliendo de NotaFácil.")

        case _:
            print("Opción inválida.")