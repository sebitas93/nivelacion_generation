# Nivelación Generation - Fundamentos de Programación

Este repositorio contiene ejercicios prácticos de nivelación en Python, enfocados en reforzar los fundamentos de programación aplicados al soporte técnico. Los ejercicios están organizados por nivel de dificultad: básico e intermedio.

---

##Contenido

###Nivel Básico

- **ejercicio1.py**  
  Verificación de acceso con contraseña. Pide al usuario una clave e indica si es correcta comparándola con una contraseña predefinida (`"admin123"`).

- **ejercicio2.py**  
  Evaluación del espacio libre en disco. Solicita al usuario la cantidad de espacio disponible en GB y muestra alertas según el nivel de criticidad (bajo, medio o adecuado).

- **ejercicio3.py**  
  Conversión de unidades de almacenamiento. Convierte una cantidad de bytes ingresada por el usuario a kilobytes (KB), megabytes (MB) y gigabytes (GB), usando el sistema binario (divisiones por 1024).

---

### Nivel Intermedio

- **ejercicio_intermedio.py**  
  Verificación de seguridad de contraseñas. Comprueba que una contraseña cumpla con los siguientes requisitos:
  - Al menos 8 caracteres
  - Al menos un número
  - Al menos una letra mayúscula
  - Al menos un símbolo especial (como `!`, `@`, etc.)

  Además:
  - La contraseña se ingresa de forma oculta usando `getpass`
  - El usuario puede reintentar hasta que la contraseña sea válida

---

## Cómo ejecutar

1. Asegúrate de tener Python instalado (versión 3.10 o superior recomendada).
2. Abre una terminal en la carpeta donde están los archivos.
3. Ejecuta cualquiera de los scripts. Ejemplo:

```bash
python ejercicio1.py
