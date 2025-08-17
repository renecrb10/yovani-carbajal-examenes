import random

"Generar lista con números aleatorios"
def generar_lista(aleatorio, indice):
    if not isinstance(aleatorio, int):
        print("El numero aleatorio debe ser un número entero")
        return []

    lista = [random.randint(1, 100) for _ in range(aleatorio)]
    print("Lista generada:", lista)

    # validar índice
    if 0 <= indice < len(lista):
        print("El valor en el índice {} es: {}".format(indice, lista[indice]))
    else:
        print("El índice no existe en la lista")

    return lista


# 2. Obtener números no repetidos
def numeros_no_repetidos(lista):
    no_repetidos = list(set(lista))
    print("Números no repetidos:", no_repetidos)
    return no_repetidos


# 3. Ordenar de mayor a menor y menor a mayor
def ordenar_lista(lista):
    mayor_a_menor = sorted(lista, reverse=True)
    menor_a_mayor = sorted(lista)
    print("Ordenada mayor a menor:", mayor_a_menor)
    print("Ordenada menor a mayor:", menor_a_mayor)
    return mayor_a_menor, menor_a_mayor


# 4. Mayor número par
def mayor_par(lista):
    pares = [n for n in lista if n % 2 == 0]
    if pares:
        mayor = max(pares)
        print("Mayor número par:", mayor)
        return mayor
    else:
        print("No hay números pares en la lista")
        return None


" Aui probaremos nuestro codigo implementado"
if __name__ == "__main__":
    lista = generar_lista(8, 3)
    no_repe = numeros_no_repetidos(lista)
    ordenar_lista(no_repe)
    mayor_par(no_repe)