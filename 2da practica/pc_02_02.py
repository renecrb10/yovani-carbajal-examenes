"""2.
Usando el concepto de funciones (3 ptos):
"""

"Crear una función normalizar_nombres(nombres)"

def normalizar_nombres(nombres):
    """
    Recibe una lista de strings y devuelve la lista normalizada.
    Debe contener al menos 6 elementos.
    """
    "El parámetro recibe una lista de string de nombres (6 como mínimo)"
    if len(nombres) < 6:
        raise ValueError("La lista debe contener al menos 6 nombres.")
    "Realizaoms una copioa para no alterar el original"

    copia_nombres = nombres[:]
    nombres_normalizados = []
    duplicado = set()
    "Quitar el espacio antes y después si lo hubiera y tipo titulo"
    for nombre in copia_nombres:
        sin_espacios = nombre.strip().title()
        "Si hubiera más nombre los debe separar (si debe haber el caso)"
        separar = sin_espacios.split()
        for separa in separar:
            if separa not in duplicado:
                duplicado.add(separa)
                nombres_normalizados.append(separa)

    return nombres_normalizados

lista_nombres = [
        "   Yovani edgar ", "karla judith", "yovani carlos", "karla jenny", "maria judith", "luis yovani", "JOSE"
    ]

resultado = normalizar_nombres(lista_nombres)

print("Lista nombres:", lista_nombres)
print("Lista normalizada:", resultado)