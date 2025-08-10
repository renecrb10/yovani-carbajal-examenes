#INGRESAMOS LOS DATOS
total_cuenta = float(input("Total de la cuenta a pagar: S/. "))
porcentaje_propina = float(input("Cuanto de porcentaje de propinas quieres dejar: % "))
numero_personas = int(input("Número de personas que pagaran la cuenta: "))

monto_propina = total_cuenta * (porcentaje_propina / 100)
monto_total = total_cuenta + monto_propina

# Cálculo del monto por persona
monto_por_persona = monto_total / numero_personas

# Salida de resultados
print(f"\nMonto total con propina: S/. {monto_total:.2f}")
print(f"Cada persona debe pagar: S/. {monto_por_persona:.2f}")

# Advertencia si el monto por persona supera los S/. 100
if monto_por_persona > 100:
    print("¡Advertencia! El monto por persona supera los S/. 100")