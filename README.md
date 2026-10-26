# Sistema de Gestión de Notas - NotaFácil

## Datos del proyecto

### Alumna

- Malena Aguirre

### Lenguaje utilizado

- 🐍 Python

## 📝 Descripción del código

El sistema desarrollado es una aplicación de consola que permite gestionar las notas de los alumnos de un curso del Instituto Horizonte, hecho basándose en las solicitudes de Laura, su coordinadora. A través de un menú interactivo, se pueden cargar alumnos, consultar sus calificaciones, calcular promedios y obtener estadísticas generales del curso.

### 🎯 Objetivos

- Registrar alumnos y sus notas de ambos parciales.
- Validar los datos ingresados por el usuario.
- Calcular los promedios individuales y el promedio general del curso.
- Identificar el mejor y el peor promedio.
- Contabilizar los alumnos que promocionan, aprueban y desaprueban.
- Generar un ranking ordenado según los promedios.
- Buscar alumnos por nombre.
- Analizar nombres mediante el conteo de vocales y la inversión de sus caracteres.

### ⚙️ Funcionalidades implementadas

1. **📥 Cargar alumnos:** solicita la cantidad de alumnos, sus nombres y las notas de ambos parciales. Valida que los datos ingresados sean correctos.
2. **📋 Mostrar listado:** muestra el nombre de cada alumno, sus dos notas y su promedio.
3. **📊 Mostrar estadísticas:** calcula el promedio general del curso, identifica el mejor y el peor promedio y cuenta cuántos alumnos promocionan, aprueban y desaprueban.
4. **🏆 Ver ranking:** ordena a los alumnos de mayor a menor promedio mediante el algoritmo de burbuja, manteniendo relacionados sus nombres y calificaciones.
5. **🔎 Buscar alumno:** permite ingresar un nombre y consultar sus notas y promedio. Si no existe, informa al usuario.
6. **🔤 Analizar un nombre:** cuenta las vocales y muestra el nombre ingresado en orden inverso.
7. **🚪 Salir:** finaliza la ejecución del programa.

### 🗂️ Organización del proyecto

El proyecto se encuentra dividido en tres módulos:

- `main.py`: contiene el menú principal y el flujo del programa.
- `validaciones.py`: contiene las funciones encargadas de validar los nombres, las notas y la cantidad de alumnos.
- `procesamiento.py`: contiene las funciones para calcular promedios, obtener estadísticas, ordenar los alumnos y analizar cadenas de caracteres.


## 🔄 Flujo del programa
### Para ejecutar el programa, es necesario tener Python instalado y abrir el proyecto en un editor de código, como Visual Studio Code. Luego, ejecutar el archivo main.py y seguir las instrucciones del menú.

Se muestra el menú principal.
El usuario selecciona una opción.
Si elige cargar alumnos, se solicitan y validan los datos.
Se calculan y almacenan los promedios individuales.
Según la opción seleccionada, se muestran los listados, las estadísticas, el ranking o los resultados de las búsquedas y el análisis de nombres.
El menú vuelve a mostrarse hasta que el usuario selecciona la opción de salir.

## ☆¡Gracias por leer!☆