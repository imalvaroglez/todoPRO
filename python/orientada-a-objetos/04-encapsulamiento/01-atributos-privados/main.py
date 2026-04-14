# Encapsulamiento (Encapsulation) en Python
# Proteger los datos internos de una clase y controlar su acceso

# Encapsulamiento básico con getters y setters
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial  # El guion bajo (_) indica que es privado

    # Getter - permite leer el saldo
    def get_saldo(self):
        return self._saldo

    # Setter con validación - controla cómo se modifica el saldo
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            return True
        else:
            return False

    def retirar(self, monto):
        if monto > 0 and self._saldo >= monto:
            self._saldo -= monto
            return True
        else:
            return False


# Uso de la clase encapsulada
cuenta = CuentaBancaria(1000)

print(f"Saldo inicial: ${cuenta.get_saldo()}")

# Intentar retirar más de lo que hay (debe fallar)
resultado = cuenta.retirar(500)
print(f"¿Retiró 500? {resultado}")
print(f"Saldo actual: ${cuenta.get_saldo()}")

# Depositar dinero
resultado = cuenta.depositar(200)
print(f"¿Depositó 200? {resultado}")
print(f"Saldo actual: ${cuenta.get_saldo()}")

# Retirar dinero válido
resultado = cuenta.retirar(300)
print(f"¿Retiró 300? {resultado}")
print(f"Saldo actual: ${cuenta.get_saldo()}")


# Encapsulamiento con @property (Python moderno)
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("La edad no puede ser negativa")


p = Persona("Juan", 25)
print(f"Nombre: {p.nombre}, Edad: {p.edad}")

p.nombre = "María"
print(f"Nuevo nombre: {p.nombre}")

p.edad = 30  # Validación en el setter
print(f"Nueva edad: {p.edad}")
