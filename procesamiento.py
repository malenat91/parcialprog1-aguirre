from validaciones import (
    validar_cantidad_alumnos,
    validar_nombre,
    validar_nota
)

def calcular_promedios(
    notas_parcial_1: list[int],
    notas_parcial_2: list[int]
) -> list[float]:
    """
    Calcula el promedio de cada alumno y
    guarda cada promedio en una lista

    args:
        notas_parcial_1: list[int], notas del primer parcial.
        notas_parcial_2: list[int], notas del segundo parcial.

    returns:
        Devuelve una lista con los promedios.
    """
    promedios = []

    for i in range(len(notas_parcial_1)):
        promedio = (notas_parcial_1[i] + notas_parcial_2[i]) / 2
        promedios = promedios + [promedio]

    return promedios


def cargar_alumnos() -> tuple[list[str], list[int], list[int], list[float]]:
    """
    Carga los datos de los alumnos y calcula sus promedios.

    returns:
        Devuelve cuatro listas:
        -nombres: nombres de los alumnos
        -notas_parcial_1: notas del primer parcial
        -notas_parcial_2: notas del segundo parcial
        -promedios: promedios de los alumnos
    """

    nombres = []
    notas_parcial_1 = []
    notas_parcial_2 = []

    cantidad = validar_cantidad_alumnos()

    for i in range(cantidad):
        nombre = validar_nombre()
        nota_1 = validar_nota(1) #nota de parcial 1
        nota_2 = validar_nota(2) #nota de parcial 2

        nombres = nombres + [nombre]
        notas_parcial_1 = notas_parcial_1 + [nota_1]
        notas_parcial_2 = notas_parcial_2 + [nota_2]

    promedios = calcular_promedios(notas_parcial_1, notas_parcial_2)

    return nombres, notas_parcial_1, notas_parcial_2, promedios




def mostrar_listado(
    nombres: list[str],
    notas_parcial_1: list[int],
    notas_parcial_2: list[int],
    promedios: list[float]
) -> None:
    """
    Muestra el listado de alumnos con nombre,
    notas y promedio.

    args:
        nombres: list[str], nombres de los alumnos.
        notas_parcial_1: list[int], notas del primer parcial.
        notas_parcial_2: list[int], notas del segundo parcial.
        promedios: list[float], promedios de los alumnos.

    returns:
        No devuelve ningún valor. Muestra el listado.
    """
    print("Listado de alumnos:")

    for i in range(len(nombres)):
        print(
        nombres[i],
        "| Parcial 1:", notas_parcial_1[i],
        "| Parcial 2:", notas_parcial_2[i],
        "| Promedio:", promedios[i])


def mostrar_estadisticas(
    nombres: list[str],
    promedios: list[float]
) -> None:
    """
    Calcula y muestra las estadísticas del curso:
    -el promedio general
    -el alumno con el mejor promedio
    -el alumno con el peor promedio
    -los alumnos que promocionan con promedio mayor o igual a 6
    -los alumnos que aprueban con promedio desde 4 hasta menos de 6
    -los alumnos que desaprueban con promedio menor a 4

    args:
        nombres: list[str], nombres de los alumnos.
        promedios: list[float], promedios de los alumnos.

    returns:
        No devuelve ningún valor. Muestra las estadísticas.
    """
    acumulador = 0
    mejor_nota = 0
    peor_nota = 0
    promocionan = 0
    aprueban = 0
    desaprueban = 0

    for i in range(len(promedios)):
        acumulador = acumulador + promedios[i]

        if promedios[i] > promedios[mejor_nota]:
            mejor_nota = i

        if promedios[i] < promedios[peor_nota]:
            peor_nota = i

        if promedios[i] >= 6:
            promocionan = promocionan + 1

        elif promedios[i] >= 4:
            aprueban = aprueban + 1
            
        else:
            desaprueban = desaprueban + 1

    promedio_general = acumulador / len(promedios)

    print("Estadisticas del curso:")
    print("Promedio general:", promedio_general)
    print("Mejor promedio:", nombres[mejor_nota], promedios[mejor_nota])
    print("Peor promedio:", nombres[peor_nota], promedios[peor_nota])
    print("Promocionan:", promocionan)
    print("Aprueban:", aprueban)
    print("Desaprueban:", desaprueban)


def ordenar_por_promedio(
    nombres: list[str],
    notas_parcial_1: list[int],
    notas_parcial_2: list[int],
    promedios: list[float]
) -> None:
    """
    Ordena el listado de alumnos por promedio de mayor a menor:
    -copia las listas originales
    -utiliza el método de ordenamiento burbuja
    -ordena los promedios de mayor a menor
    -intercambia los nombres y las notas para mantener los datos
    de cada alumno relacionados
    -muestra el listado ordenado sin modificar las listas originales

    args:
        nombres: list[str], nombres de los alumnos.
        notas_parcial_1: list[int], notas del primer parcial.
        notas_parcial_2: list[int], notas del segundo parcial.
        promedios: list[float], promedios de los alumnos.

    returns:
        No devuelve ningún valor. Muestra (print) el ranking ordenado
        sin modificar las listas originales.
    """
    nombres_copia = []
    notas_1_copia = []
    notas_2_copia = []
    promedios_copia = []

    for i in range(len(nombres)):
        nombres_copia = nombres_copia + [nombres[i]]
        notas_1_copia = notas_1_copia + [notas_parcial_1[i]]
        notas_2_copia = notas_2_copia + [notas_parcial_2[i]]
        promedios_copia = promedios_copia + [promedios[i]]

    for i in range(len(promedios_copia) - 1): #i marca la pasada/vuelta
        for j in range(len(promedios_copia) - 1 - i): #j marca la posicion que se compara con la sig
            if promedios_copia[j] < promedios_copia[j + 1]:
                auxiliar = promedios_copia[j]
                promedios_copia[j] = promedios_copia[j + 1]
                promedios_copia[j + 1] = auxiliar

                auxiliar = nombres_copia[j]
                nombres_copia[j] = nombres_copia[j + 1]
                nombres_copia[j + 1] = auxiliar

                auxiliar = notas_1_copia[j]
                notas_1_copia[j] = notas_1_copia[j + 1]
                notas_1_copia[j + 1] = auxiliar

                auxiliar = notas_2_copia[j]
                notas_2_copia[j] = notas_2_copia[j + 1]
                notas_2_copia[j + 1] = auxiliar

    mostrar_listado(
        nombres_copia,
        notas_1_copia,
        notas_2_copia,
        promedios_copia
    )


def buscar_alumno(
    nombres: list[str],
    notas_parcial_1: list[int],
    notas_parcial_2: list[int],
    promedios: list[float]
) -> None:
    """
    Busca un alumno dentro del listado:
    -solicita el nombre del alumno que se desea buscar
    -recorre la lista de nombres
    -compara los nombres con el nombre ingresado
    -si lo encuentra, muestra sus notas y promedio
    -si no lo encuentra, informa que el alumno no existe

    args:
        nombres: list[str], nombres de los alumnos.
        notas_parcial_1: list[int], notas del primer parcial.
        notas_parcial_2: list[int], notas del segundo parcial.
        promedios: list[float], promedios de los alumnos.

    returns:
        No devuelve ningún valor. Muestra los datos
        del alumno o un mensaje indicando que no existe.
    """
    nombre_buscado = input("Ingrese el nombre del alumno: ")
    indice = -1

    for i in range(len(nombres)):
        if nombres[i] == nombre_buscado:
            indice = i

    if indice == -1:
        print("El alumno no existe.")
    else:
        print("Informacion del alumno: ")
        print("Nombre:", nombres[indice])
        print("Nota del parcial 1:", notas_parcial_1[indice])
        print("Nota del parcial 2:", notas_parcial_2[indice])
        print("Promedio:", promedios[indice])


def analizar_nombre() -> None:
    """
    Analiza un nombre ingresado:
    -cuenta la cantidad de vocales
    -construye el nombre en orden inverso
    -muestra la cantidad de vocales encontradas
    -muestra el nombre invertido

    returns:
        No devuelve ningún valor. Muestra (print) los resultados.
    """
    nombre = input("Ingrese un nombre: ")
    cantidad_vocales = 0
    invertido = ""

    for i in range(len(nombre)):
        caracter = nombre[i]

        if (
            caracter == "a" or caracter == "e"
            or caracter == "i" or caracter == "o"
            or caracter == "u" or caracter == "A"
            or caracter == "E" or caracter == "I"
            or caracter == "O" or caracter == "U"
        ):
            cantidad_vocales = cantidad_vocales + 1

    for i in range(len(nombre) - 1, -1, -1):
        invertido = invertido + nombre[i]

    print(f"Nombre del alumnx: " + nombre)
    print("Cantidad de vocales:", cantidad_vocales)
    print("Nombre invertido:", invertido)