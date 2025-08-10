"""1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
un diccionario donde las claves serán los nombres de los estudiantes y sus
valores serán listas con 3 notas
"""

def procesar_notas(estudiantes):

    notas = {}
    return notas


estudiantes = {
    "yovani": [16, 18, 14],
    "Jorge": [10, 11, 11],
    "Melissa": [9, 7, 5],
}
notas_est = procesar_notas(estudiantes)



"""Calcular el promedio de cada estudiantes."""
def procesar_notas(estudiantes):
    resultado = {}

    for nombre, notas in estudiantes.items():
        # Calcula el promedio usando sumatoria y cantidad de notas
        promedio = sum(notas) / len(notas)
        resultado[nombre] = promedio

    return resultado


# Llamada a la función
notas_prom = procesar_notas(estudiantes)
print(notas_prom)


""" Devolver un nuevo diccionario donde la clave sea el nombre 
del estudiante y el valor sea otro diccionario con:
promedio: que será el promedio de notas
estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor """
def procesar_notas(estudiantes):
    resultado = {}

    for nombre, notas in estudiantes.items():
        promedio = sum(notas) / len(notas)
        estado = "aprobado" if promedio >= 11 else "desaprobado"

        resultado[nombre] = {
            "promedio": round(promedio, 2),
            "estado": estado
        }

    return resultado

"Imprimimos el diccionario de estudiantes"
dicionario_estudiantes = procesar_notas(estudiantes)
print(dicionario_estudiantes)

"""Mostrar en pantalla el estudiante con mayor promedio"""
mejor_est = max(dicionario_estudiantes, key=lambda nombre: dicionario_estudiantes[nombre]["promedio"])
print(f"El estudiante con mayor promedio es {mejor_est} con {dicionario_estudiantes[mejor_est]['promedio']}")
