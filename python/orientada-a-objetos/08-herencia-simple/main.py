# Herencia en Python

# Clase base (Padre)
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo...")

    def dormir(self):
        print(f"{self.nombre} está durmiendo...")

# Clase derivada (Hija) de Animal
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llamar al constructor de la clase padre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau, guau!")

    def traer_pelota(self):
        print(f"{self.nombre} trae la pelota con entusiasmo")

# Clase derivada (Hija) de Animal
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau!")

    def ronronear(self):
        print(f"{self.nombre} ronronea felizmente...")

# Clase derivada (Hija) de Animal
class Pajaro(Animal):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo

    def volar(self):
        print(f"{self.nombre} vuela alto en el cielo")

    def cantar(self):
        print(f"{self.nombre} canta hermosamente")

print("--- Ejemplo 1: Perro ---")
perro = Perro("Firulais", "Golden Retriever")
print(f"Nombre: {perro.nombre}, Raza: {perro.raza}")
perro.comer()      # Método heredado de Animal
perro.ladrar()     # Método propio de Perro
perro.dormir()     # Método heredado de Animal

print("\n--- Ejemplo 2: Gato ---")
gato = Gato("Michi", "Naranja")
print(f"Nombre: {gato.nombre}, Color: {gato.color}")
gato.comer()       # Método heredado de Animal
gato.maullar()     # Método propio de Gato
gato.ronronear()   # Método propio de Gato

print("\n--- Ejemplo 3: Pájaro ---")
pajaro = Pajaro("Tweety", "Canario")
print(f"Nombre: {pajaro.nombre}, Tipo: {pajaro.tipo}")
pajaro.comer()      # Método heredado de Animal
pajaro.volar()      # Método propio de Pájaro
pajaro.cantar()     # Método propio de Pájaro

# Ejemplo práctico: Sistema de empleados
print("\n--- Ejemplo 4: Sistema de Empleados ---")

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def trabajar(self):
        print(f"{self.nombre} está trabajando...")

    def cobrar_sueldo(self):
        print(f"{self.nombre} cobra su sueldo de ${self.sueldo}")

class Programador(Empleado):
    def __init__(self, nombre, sueldo, lenguaje):
        super().__init__(nombre, sueldo)
        self.lenguaje = lenguaje

    def programar(self):
        print(f"{self.nombre} está programando en {self.lenguaje}...")

    def depurar(self):
        print(f"{self.nombre} está depurando código...")

class Disenador(Empleado):
    def __init__(self, nombre, sueldo, herramienta):
        super().__init__(nombre, sueldo)
        self.herramienta = herramienta

    def disenar(self):
        print(f"{self.nombre} está diseñando con {self.herramienta}...")

    def crear_mockup(self):
        print(f"{self.nombre} está creando un mockup...")

# Crear empleados
programador = Programador("Carlos", 25000, "Python")
disenador = Disenador("Ana", 22000, "Figma")

print("Programador:")
programador.trabajar()      # Método heredado
programador.programar()    # Método propio
programador.depurar()      # Método propio
programador.cobrar_sueldo() # Método heredado

print("\nDiseñador:")
disenador.trabajar()      # Método heredado
disenador.disenar()      # Método propio
disenador.crear_mockup() # Método propio
disenador.cobrar_sueldo() # Método heredado
