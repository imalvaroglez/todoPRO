# Cómo subir todoPRO a GitHub

El repo ya existe en: https://github.com/imalvaroglez/todoPRO

## Paso 1: Instalar Git (si no lo tienes)

**En Windows:**
1. Descarga Git desde: https://git-scm.com/download/win
2. Instala Git (usa las opciones por defecto)
3. Verifica la instalación: Abre CMD o PowerShell y escribe:
   ```bash
   git --version
   ```

## Paso 2: Abrir terminal en la carpeta del proyecto

Abre CMD o PowerShell y navega a la carpeta del proyecto:

```bash
cd C:\Users\tu_usuario\AppData\Local\Temp\todoPRO10
```

*Nota: La ruta puede variar. Mejor abre la carpeta en el Explorador de Archivos, haz clic derecho en un espacio vacío y selecciona "Abrir en Terminal"*

## Paso 3: Inicializar Git y preparar el primer commit

```bash
git init
git add .
git commit -m "Initial commit: todoPRO - Curso de programación de 0 a 100"
```

## Paso 4: Conectar con el repositorio remoto de GitHub

```bash
git remote add origin https://github.com/imalvaroglez/todoPRO.git
git branch -M main
git push -u origin main
```

**¡Eso es todo!** Tu proyecto estará en GitHub.

---

## Nota importante: Autenticación

La primera vez que hagas `git push`, GitHub te pedirá:

**Si tienes autenticación con contraseña:**
- Usuario: tu nombre de usuario de GitHub
- Contraseña: **NO es tu contraseña de GitHub**. Necesitas un **Personal Access Token**

**Cómo crear un Personal Access Token:**

1. Ve a: https://github.com/settings/tokens
2. Clic en "Generate new token" (clásic)
3. Ponle un nombre: "todoPRO upload"
4. Selecciona los permisos:
   - ✅ repo (control completo de repositorios privados)
   - ✅ workflow (permisos de GitHub Actions)
5. Genera el token
6. **COPIA EL TOKEN** (no podrás verlo otra vez)

7. Cuando git pida contraseña, pega el token

**Si tienes autenticación con SSH:**
- Si ya configuraste SSH, solo se usará tu llave SSH
- No necesitarás token

---

## Para futuros cambios (cuando agregues más ejemplos Python)

```bash
cd C:\ruta\a\todoPRO10
git add .
git commit -m "Agregados ejemplos de POO básico"
git push
```

---

## Verificar que funcionó

Ve a: https://github.com/imalvaroglez/todoPRO

Deberías ver:
- La carpeta `cpp/` con todo el contenido original de todoPRO10.zip
- La carpeta `python/` con los ejemplos adaptados
- El archivo `README.md` con las instrucciones

🚀 ¡Listo!
