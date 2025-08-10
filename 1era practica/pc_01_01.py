#Asignar en variables los datos de tu nombre, salario, edad y compañía para un usuario
#voy a definir las variables
nombre = "Yovani Carbajal Ochoa"
salario = 3800
edad = "32"
compania = "UNSCH"

#identificar sus tipos de variables
print("Tipo de variable 'nombre':", type(nombre))
print("Tipo de variable 'salario':", type(salario))
print("Tipo de  variable 'edad':", type(edad))
print("Tipo de variable 'compania':", type(compania))

#Identificar si la edad es mayor a 30, mostrar un mensaje ingresado
# “Usted tiene un bono de 10% en el mes de diciembre” caso contrario
# mostrar “Usted tiene un bono del 5% en el mes diciembre”
# paso 01 convertimos la edad a entero
edad_entero = int(edad)

#Paso 02 Bono segun edad
if edad_entero > 30:
    bono_porcentaje = 0.10
    print("Usted es afortunado, tiene un bono de 10% para el mes de diciembre")
else:
    bono_porcentaje = 0.05
    print(" Tienes un bono del 5% en el mes de diciembre")

#Paso 03 Mostrar el bono final
#Duplicamos el salario ( a lo que entiendo es duplicar el salario y no potenciarlo)
potencia_salario = salario *2
# Bono extra
bono_extra = salario * bono_porcentaje
# Bono final total
bono_final = potencia_salario + bono_extra

# Mostramos el sueldo final
print("su bono final  :", bono_final)





