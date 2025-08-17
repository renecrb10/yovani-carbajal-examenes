from datetime import datetime

"Primero definos el decorador"
def mi_decorador(funcion):
    def wrapper(*args):
        # mostrar hora actual
        ahora = datetime.now()
        print("El decorador está siendo ejecutado a las {} horas con {} minutos y {} segundos"
              .format(ahora.hour, ahora.minute, ahora.second))

        # ejecutar la función decorada
        resultado = funcion(*args)

        # suma de los elementos
        total = sum(args)
        print("La suma de todos los valores es:", total)

        return resultado
    return wrapper


"Definiom la fncion decorada"
@mi_decorador
def mayor_numero(a, b, c, d, e, f):
    mayor = max(a, b, c, d, e, f)
    print("El mayor número es:", mayor)
    return mayor


"uSMAOS CON ESTOS DATOS"
mayor_numero(10, 20, 5, 40, 7, 15)