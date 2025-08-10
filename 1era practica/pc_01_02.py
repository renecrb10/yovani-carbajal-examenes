#definos las notas de los alumonos
matematicas = 17
ciencia = 14
historia = 15

# se define el porcentake de peso de cada curso  Matemáticas: 40%, Ciencia: 30%, Historia: 30%
peso_matematicas = 0.40
peso_ciencia = 0.30
peso_historia = 0.30

# calculamos la nota final ponderada del alumno.
nota_final = (matematicas * peso_matematicas + ciencia * peso_ciencia + historia * peso_historia)

#redondeamos la nota del alumno
nota_final_redondeada = round(nota_final, 1)

# Aprobado, si es mayor igual a 13
aprobado = nota_final_redondeada >= 13.0

# Mostrar resultados
print(f"La nota final es: {nota_final_redondeada}")
print(f"¿Aprobado?: {aprobado}")

# generamos el resumen de las si eta aprobado o no ,
estado = "Aprobado" if aprobado else "Desaprobado"
print(f"El estudiante obtuvo una nota final de {nota_final_redondeada} y su estado final es: {estado}")