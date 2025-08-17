"""Crear una clase llamada Empleado donde sus atributos
deben ser nombre, edad, sueldo y de nacionalidad peruana,
tendrá un método para solicitar su nombre y otro para solicitar
su edad. Así como un método cumpleaños donde cada vez que invoque
aumentará en un año la edad de la persona."""

class Empleado:
    "nacionalidad por defecto: Peruana"
    def __init__(self, nombre, edad, sueldo, nacionalidad="Peruana"):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = float(sueldo)
        self.nacionalidad = nacionalidad
    "ACTUALZIACION NOM,BRE POR CONSOLA"
    def solicitar_nombre(self):
        nuevo = input("Ingrese nombre: ").strip().title()
        if nuevo:
            self.nombre = nuevo
    "ACTUALZIAOCN EDAD POR CONSOLA"


    def solicitar_edad(self):
        try:
            nueva = int(input("Ingrese edad: ").strip())
            if nueva >= 0:
                self.edad = nueva
        except ValueError:
            print("Edad inválida")

    "Aumento de cumpleaños en un año"


    def cumpleanios(self):
        self.edad = self.edad + 1


    "Aumento de sueldo en 30 %"

    def aumentoSueldo(self, porcentaje=0.30):
        if porcentaje < 0:
            return
        self.sueldo = round(self.sueldo * (1 + porcentaje), 2)


    "Validar edad y devolver mensaje"

    def prediccion(self, anio, edad_ingresada):
        if edad_ingresada < self.edad:
            return "No es posible realizar la operación"
        return "En el año {} tendrá {} años".format(anio, edad_ingresada)


    "Hrencia: Persona va heredar de empleado y va agregar saldo"

class Persona(Empleado):
    def __init__(self, nombre, edad, sueldo, saldo=0.0, nacionalidad="Peruana"):
        super().__init__(nombre, edad, sueldo, nacionalidad)
        self.saldo = float(saldo)

    def mostrar_saldo(self):
        print("Saldo actual de {}: S/ {:.2f}".format(self.nombre, self.saldo))

    # transferencia entre personas
    def transferencia(self, otro, monto):
        if not isinstance(otro, Persona):
            print("Solo se puede transferir a otra Persona")
            return
        if monto <= 0:
            print("El monto debe ser mayor a 0")
            return
        if self.saldo < monto:
            print("Saldo insuficiente")
            return
        self.saldo = self.saldo - monto
        otro.saldo = otro.saldo + monto
        print("Transferencia: {} → {} por S/ {:.2f}".format(self.nombre, otro.nombre, monto))
        self.mostrar_saldo()
        otro.mostrar_saldo()


"COMPRORABACION"
if __name__ == "__main__":
    emp1 = Persona("Yovani", 30, 2000, saldo=500)
    emp2 = Persona("Melissa", 28, 1800, saldo=200)

    # cumpleaños
    emp1.cumpleanios()
    emp2.cumpleanios()

    # aumento 30% y mostrar
    emp1.aumentoSueldo()
    emp2.aumentoSueldo()
    print("Sueldo actualizado de {}: S/ {:.2f}".format(emp1.nombre, emp1.sueldo))
    print("Sueldo actualizado de {}: S/ {:.2f}".format(emp2.nombre, emp2.sueldo))

    # predicción (válida e inválida)
    print(emp1.prediccion(2030, 36))   # ok
    print(emp1.prediccion(2030, 25))   # no posible

    # transferencia válida
    emp1.mostrar_saldo()
    emp2.mostrar_saldo()
    emp1.transferencia(emp2, 150)

    # intento con saldo insuficiente
    emp2.transferencia(emp1, 1000)
