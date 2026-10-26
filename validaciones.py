def validar_cantidad_alumnos() -> int:
    """
    Valida que la cantidad de alumnos cumpla con lo solicitado:
    -que sea mayor o igual a 1
    -que sea menor o igual a 30

    returns:
        Devuelve (return) una cantidad de alumnos válida.
    """

    cantidad = int(input("Ingrese la cantidad de alumnos: "))

    while cantidad < 1 or cantidad > 30:
        print("Debe ingresar entre 1 y 30 alumnos.")
        cantidad = int(input("Ingrese la cantidad de alumnos: "))

    return cantidad


def validar_nota(numero_parcial: int) -> int:
    """
    Valida que la nota esté entre 0 y 10.

    args:
    numero_parcial: int, número del parcial cuya nota se solicita.

    returns:
    Devuelve una nota válida.

    """

    nota = int(input("Ingrese la nota del parcial " + str(numero_parcial) + ": "))

    while nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10.")
        nota = int(input("Ingrese la nota del parcial " + str(numero_parcial) + ": "))

    return nota


def validar_nombre() -> str:
    """
    Valida que el nombre del alumno cumpla con todo lo solicitado:
    - Que tenga al menos 5 caracteres.
    - Que contenga solamente letras mayúsculas, minúsculas o espacios.
    - Que no contenga números ni otros caracteres especiales.

    returns:
        Devuelve un nombre válido.
    """

    nombre = input("Ingrese el nombre del alumno: ")
    valido = False  # bandera para controlar el while

    while valido == False:
        valido = True

        for i in range(len(nombre)):
            caracter = nombre[i]

            if not (
                caracter >= "A" and caracter <= "Z"
                or caracter >= "a" and caracter <= "z"
                or caracter == " "
            ):
                valido = False

        if len(nombre) < 5:
            print("El nombre debe tener al menos cinco caracteres.")

        elif valido == False:
            print("Ingrese un nombre usando solamente letras y espacios.")

        else:
            return nombre

        nombre = input("Ingrese el nombre del alumno: ")