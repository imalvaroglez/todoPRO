# Curso de Programación - De 0 a 100

**Bienvenido al curso de programación.** Este material está diseñado para alguien sin experiencia previa, llevándote desde lo más básico hasta la programación orientada a objetos.

---

## 📁 ESTRUCTURA DEL CURSO

Este curso tiene dos versiones:

- **`cpp/`** - Versión en C++ (más técnico, curve learning más fuerte)
- **`python/`** - Versión en Python (más fácil, ideal para empezar)

**Recomendación:** Si nunca has programado, **empieza con Python**. Es más amigable y verás resultados más rápido.

---

## 🎯 QUÉ VAS A APRENDER

El curso está dividido en **2 grandes secciones:**

### 1. Programación Estructurada y Modular
- Variables y tipos de datos
- Estructuras de control (if, else, switch)
- Bucles y repetición (for, while)
- Funciones y modularidad
- Arreglos y estructuras complejas

### 2. Programación Orientada a Objetos (POO)
- Clases y objetos
- Constructores y destructores
- Encapsulamiento
- Herencia
- Polimorfismo

---

## 💻 REQUISITOS Y SETUP (WINDOWS)

### Paso 1: Instalar Python (si elegiste la versión Python)

1. Ve a: **https://www.python.org/downloads/**
2. Descarga la versión para Windows
3. Instala Python (IMPORTANTE: marca la casilla "Add Python to PATH")
4. Verifica la instalación:
   - Abre la terminal (cmd o PowerShell)
   - Escribe: `python --version`
   - Debe mostrar algo como: `Python 3.12.0`

### Paso 2: Instalar Visual Studio Code (IDE)

**¿Qué es un IDE?** Un IDE (Integrated Development Environment) es donde escribes, depuras y ejecutas tu código. Es como un editor de texto avanzado para programar.

1. Ve a: **https://code.visualstudio.com/**
2. Descarga VS Code para Windows
3. Instala VS Code
4. Abre VS Code

### Paso 3: Configurar VS Code para Python

1. En VS Code, ve a la sección de **Extensiones** (icono de cuadrados a la izquierda)
2. Busca: **Python**
3. Instala la extensión de Microsoft (la que tiene el logo de Python)
4. Reinicia VS Code si te lo pide

### Paso 4: Configurar VS Code para C++ (si elegiste C++)

1. En VS Code, ve a la sección de **Extensiones**
2. Busca: **C/C++**
3. Instala la extensión de Microsoft
4. Instala también **C/C++ Extension Pack**
5. Necesitarás un compilador como MinGW o usar Visual Studio

---

## 🚀 TU PRIMER PROGRAMA (PYTHON)

### Ejercicio 1: Hola Mundo

1. Crea una carpeta nueva en tu escritorio llamada `mi_primer_programa`
2. Abre esa carpeta con VS Code (Archivo → Abrir Carpeta)
3. Crea un archivo nuevo: `hola_mundo.py`
4. Escribe este código:

```python
print("Hola Mundo!")
```

5. Guarda el archivo (Ctrl + S)
6. Abre la terminal en VS Code (Terminal → Nueva Terminal)
7. Ejecuta el programa:

```bash
python hola_mundo.py
```

8. Deberías ver: `Hola Mundo!`

**¡Felicidades!** Acabas de escribir tu primer programa en Python. 🎉

---

## 🚀 TU PRIMER PROGRAMA (C++)

### Ejercicio 1: Hola Mundo

1. Crea una carpeta nueva en tu escritorio llamada `mi_primer_programa_cpp`
2. Abre esa carpeta con VS Code
3. Crea un archivo nuevo: `hola_mundo.cpp`
4. Escribe este código:

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hola Mundo!" << endl;
    return 0;
}
```

5. Guarda el archivo
6. Necesitas compilar el programa (C++ se compila antes de ejecutarse):

```bash
g++ hola_mundo.cpp -o hola_mundo
```

7. Ejecuta el programa:

```bash
hola_mundo.exe
```

8. Deberías ver: `Hola Mundo!`

---

## 📚 CÓMO USAR ESTE CURSO

### 1. Empieza con la carpeta `Ejemplos PRO`

Encontrarás carpetas organizadas por tema. Cada tema tiene ejemplos que puedes copiar y ejecutar.

**Ruta para Python:**
```
python/estructurada-y-modular/01-estructuras-de-informacion-simples/01-variables-y-constantes/
```

**Ruta para C++:**
```
cpp/estructurada-y-modular/01-estructuras-de-informacion-simples/01-variables-y-constantes/
```

### 2. Ejemplos por tema

Cada carpeta tiene varios ejemplos numerados:

```
01-variables-y-constantes/
├── 01-hola-mundo/
│   └── main.py           (Python)
│   └── main.c            (C++)
├── 02-variables-tipo-entero/
├── 06-variables-reales/
├── 07-operadores-aritmeticos/
├── 09-constantes-1/
└── 16-variables-cadena/
```

**Cómo estudiar:**
1. Lee el código del ejemplo
2. Intenta entender qué hace
3. Copia el código a un archivo nuevo
4. Ejecuta el código
5. Experimenta modificándolo

### 3. Prácticas

La carpeta `Practicas/` contiene archivos PDF con ejercicios para resolver. Estos son los "trabajos" que debes entregar.

**Ruta:**
```
Practicas/Practica1.pdf
Practicas/Practica2.pdf
...
```

### 4. Tareas

La carpeta `Tareas/` contiene tareas adicionales para reforzar lo aprendido.

---

## 🎓 SECUENCIA RECOMENDADA

### Semana 1: Fundamentos
1. **Variables y Constantes** (`01-estructuras-de-informacion-simples/01-variables-y-constantes/`)
2. **Operadores Aritméticos** (mismo tema)
3. Resuelve **Practica1.pdf**

### Semana 2: Control de Flujo
1. **Estructuras de Control** (`02-estructuras-de-control/`)
2. **Iteración/Bucles** (`03-iteracion/`)
3. Resuelve **Practica2.pdf**

### Semana 3: Funciones
1. **Funciones** (`04-funciones/`)
2. Resuelve **Practica3.pdf**

### Semana 4: Estructuras de Datos
1. **Arreglos** (`05-arreglos/`)
2. **Estructuras Complejas** (`06-estructuras-de-informacion-compleja/`)
3. Resuelve **Practica4.pdf**

### Semana 5-6: Modularidad
1. **Modularidad** (`07-modularidad/`)
2. Resuelve **Practica5.pdf** y **Practica6.pdf**

### Semana 7-12: Programación Orientada a Objetos
1. **Conceptos básicos** (`orientada-a-objetos/01-conceptos-basicos/`)
2. **Constructores** (`02-constructores/`)
3. **Métodos** (`03-metodos/`)
4. **Encapsulamiento** (`04-encapsulamiento/`)
5. **Herencia** (`08-herencia-simple/`)
6. **Polimorfismo** (`10-polimorfismo/`)
7. Resuelve **Practica7.pdf** hasta **PracticaC.pdf**

---

## 💡 CONSEJOS PARA APRENDER

1. **No copies y pegues ciegamente:** Lee el código, entiéndelo, luego escríbelo tú mismo
2. **Experimenta:** Cambia valores, prueba combinaciones, rompe el código y arréglalo
3. **Pregunta:** Si algo no te queda claro, pregunta. No te estanques más de 30 minutos
4. **Practica todos los días:** Aunque sea solo 15-20 minutos, la consistencia es clave
5. **Usa los ejemplos:** Están ahí para ayudarte. Cópialos, modifícalos, aprende de ellos
6. **No te frustres:** Programar es difícil al principio. Es normal cometer muchos errores

---

## ❓ PREGUNTAS FRECUENTES

### ¿Python o C++?
- **Python:** Más fácil, menos código, más rápido para empezar
- **C++:** Más técnico, más poderoso, pero más difícil

**Recomendación:** Empieza con Python. Cuando lo domines, C++ será más fácil.

### ¿Por qué usar VS Code?
- Es gratuito
- Es el estándar de la industria
- Tiene excelentes extensiones para todos los lenguajes
- Es fácil de usar

### ¿Qué hago si tengo errores?
- Lee el error: Python te dice exactamente qué salió mal
- Busca el error en Google
- Verifica que no hay faltas de ortografía
- Revisa que las comillas y paréntesis estén balanceados

### ¿Cuánto tiempo tardaré en aprender?
- **Nivel básico:** 4-6 semanas
- **Nivel intermedio:** 2-3 meses
- **Nivel avanzado:** 6-12 meses

**Depende de cuánto practiques.** 1-2 horas diarias es ideal.

---

## 📞 NECESITAS AYUDA?

Si tienes dudas:
1. Revisa los ejemplos de la carpeta correspondiente
2. Busca el tema específico en los ejemplos
3. Modifica el código para entender qué pasa
4. Pregunta específicamente qué no entiendes

---

## 🌟 PRÓXIMOS PASOS: CUANDO TERMINES LO BÁSICO

Una vez que domines lo fundamental (variables, bucles, funciones, POO), puedes explorar recursos más avanzados:

### ¿Qué es GitHub?

**GitHub** es la plataforma más grande del mundo para alojar y compartir código. Piensa en esto:

- Es como "Google Drive" para código
- Los desarrolladores suben sus proyectos a GitHub
- Otros pueden ver, descargar, aprender y colaborar con ese código
- Es **TOTALMENTE GRATIS** y muy usado en la industria
- Muchas empresas piden ver tu perfil de GitHub cuando entrevistan

### Proyecto Recomendado: Coding Interview University

Este es un plan de estudio completo para prepararse para entrevistas técnicas en grandes empresas de tecnología (Amazon, Google, Facebook, Microsoft).

**¿Cuándo usarlo?**
- **NO AHORA:** Este proyecto es para alguien que YA SABE programar y quiere prepararse para entrevistas técnicas
- **SÍ DESPUÉS:** Cuando domines Python y entiendas bien estructuras de datos básicas

**¿Qué incluye?**
- Estructuras de datos avanzadas (árboles, grafos, heaps, hash tables)
- Algoritmos complejos (sorting, binary search, dynamic programming)
- Complejidad algorítmica (Big-O)
- Problemas de entrevista resueltos
- Libros recomendados
- Recursos de práctica (LeetCode, HackerRank, etc.)

**Enlace:** https://github.com/jwasham/coding-interview-university

### Tu Proyecto todoPRO Puede Ser un Repo de GitHub

Cuando tengas algunos proyectos interesantes (después de las primeras 4-6 semanas de estudio), considera:

1. **Crear una cuenta gratuita en GitHub.com**
2. **Subir tu carpeta todoPRO** como un repositorio
3. **Así tendrás:**
   - Un respaldo en la nube de tu código
   - Un portafolio que puedes mostrar a futuros empleadores
   - La posibilidad de que otros aprendan de tu código
   - Una forma de rastrear tu progreso como programador

**¿Por qué hacerlo?**
- Muchas empresas piden ver tu perfil de GitHub al contratar
- Tener proyectos públicos muestra que eres activo en programación
- Es la forma estándar de que los desarrolladores muestren su trabajo

---

**¡Mucha suerte en tu viaje de aprendizaje de programación!** 💻🚀

Recuerda: Todos los programadores profesionales empezaron donde tú estás ahora. La clave es la constancia y no rendirse.
