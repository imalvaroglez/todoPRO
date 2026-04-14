# Métodos de Clase y Paso de Parámetros en Python

class Circulo:
    # Constante de clase (usamos mayúsculas por convención)
    PI = 3.1416

    def __init__(self, radio, color_borde=0, color_fondo=0):
        # Constructor
        self.radio = radio
        self.color_borde = color_borde
        self.color_fondo = color_fondo

    # Métodos setters (modificadores)
    def fijar_radio(self, radio):
        self.radio = radio

    def fijar_color_borde(self, color_borde):
        self.color_borde = color_borde

    def fijar_color_fondo(self, color_fondo):
        self.color_fondo = color_fondo

    # Métodos getters (accesores)
    def dame_radio(self):
        print("invocando dame_radio()")
        return self.radio

    def dame_color_borde(self):
        print("invocando dame_color_borde()")
        return self.color_borde

    def dame_color_fondo(self):
        print("invocando dame_color_fondo()")
        return self.color_fondo

    # Método de cálculo
    def dame_area(self):
        return self.PI * self.radio * self.radio

    # Método de comparación entre objetos
    def es_igual_a(self, otro_circulo):
        if (self.radio >= otro_circulo.dame_radio() and
            self.radio <= otro_circulo.dame_radio() and
            self.color_borde == otro_circulo.dame_color_borde() and
            self.color_fondo == otro_circulo.dame_color_fondo()):
            return True
        else:
            return False


# Crear objetos y probar
c1 = Circulo(10, 11, 14)
c2 = Circulo(10, 11, 14)
c3 = Circulo(12, 11, 14)

if c1.es_igual_a(c2):
    print("c1 y c2 son iguales")
else:
    print("c1 y c2 son diferentes")

if c1.es_igual_a(c3):
    print("c1 y c3 son iguales")
else:
    print("c1 y c3 son diferentes")
