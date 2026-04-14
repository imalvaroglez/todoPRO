# Constantes de Clase (Class-Level Constants) en Python
# Valores que son compartidos por todas las instancias de una clase

class ConfiguracionApp:
    # Constantes de nivel de clase (todas las instancias las comparten)
    # Usamos mayúsculas por convención
    VERSION = "1.0.0"
    NOMBRE_APP = "Mi Aplicación"
    MAX_INTENTOS_FALLIDOS = 5
    TIEMPO_TIMEOUT = 30  # en segundos

    @classmethod
    def mostrar_configuracion(cls):
        print(f"--- {cls.NOMBRE_APP} ---")
        print(f"Versión: {cls.VERSION}")
        print(f"Intentos máximos: {cls.MAX_INTENTOS_FALLIDOS}")
        print(f"Timeout: {cls.TIEMPO_TIMEOUT}s")


# Uso de las constantes de clase
ConfiguracionApp.mostrar_configuracion()

class Usuario:
    # Constantes específicas para usuarios
    ROL_ADMIN = "admin"
    ROL_USUARIO = "usuario"
    ESTADO_ACTIVO = "activo"
    ESTADO_INACTIVO = "inactivo"

    def __init__(self, nombre, rol=ROL_USUARIO):
        self.nombre = nombre
        self.rol = rol
        self.estado = self.ESTADO_ACTIVO

    def activar(self):
        self.estado = self.ESTADO_ACTIVO
        return True

    def desactivar(self):
        self.estado = self.ESTADO_INACTIVO
        return True

    def mostrar_info(self):
        print(f"Usuario: {self.nombre}")
        print(f"Rol: {self.rol}")
        print(f"Estado: {self.estado}")


# Demostración
admin = Usuario("Admin", Usuario.ROL_ADMIN)
usuario_normal = Usuario("Juan", Usuario.ROL_USUARIO)

print("--- Constantes de clase ---")
ConfiguracionApp.mostrar_configuracion()

print("\n--- Usuario administrador ---")
admin.mostrar_info()

print("\n--- Usuario normal ---")
usuario_normal.mostrar_info()

# Cambiar estado
usuario_normal.desactivar()
print("\n--- Después de desactivar ---")
usuario_normal.mostrar_info()

admin.activar()
print("\n--- Admin activado ---")
admin.mostrar_info()
