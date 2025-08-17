import random
"funcion para almacenar nuemros aleatorios"


def generar_lista(x):
    if not isinstance(x, int):
        raise ValueError("X debe ser un número entero")
    lista = [random.randint(1, 100) for _ in range(x)]
    print("Lista generada:", lista)
    return lista

"funcion qeu almacena numeors repetidos"
def numeros_no_repetidos(lista):
    no_repetidos = list(set(lista))
    print("Números no repetidos:", no_repetidos)
    return no_repetidos

"funcion para ordenar de mayor amenor"
def ordenar_lista(lista):
    mayor_a_menor = sorted(lista, reverse=True)
    menor_a_mayor = sorted(lista)
    print("Ordenada mayor a menor:", mayor_a_menor)
    print("Ordenada menor a mayor:", menor_a_mayor)
    return mayor_a_menor, menor_a_mayor

"funcion para indicar el mayor nuemro par"
def mayor_par(lista):
    pares = [n for n in lista if n % 2 == 0]
    if pares:
        mayor = max(pares)
        print("Mayor número par:", mayor)
        return mayor
    else:
        print("No hay números pares en la lista")
        return None

