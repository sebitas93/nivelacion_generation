# 🧠 Nivelación Generation - Fundamentos de Programación

Este repositorio contiene una serie de ejercicios prácticos en Python enfocados en fortalecer los fundamentos de programación aplicados al soporte técnico. Están organizados por nivel de dificultad: **básico**, **intermedio** y **avanzado**.

Cada script fue creado paso a paso y probado en consola. Algunos incluyen validaciones, menús interactivos y simulaciones de situaciones reales del entorno IT.

---

## 📂 Contenido

### 🔰 Nivel Básico

- **ejercicio1.py**  
  Verifica si la contraseña ingresada por el usuario coincide con una clave predefinida (`admin123`).  
  👉 Utiliza comparación simple con `if` para permitir o denegar el acceso.

- **ejercicio2.py**  
  Solicita al usuario cuántos GB libres hay en el disco e imprime un mensaje de alerta según tres rangos definidos:  
  - Menos de 10 GB → alerta crítica  
  - Entre 10 y 50 GB → advertencia  
  - Más de 50 GB → estado adecuado  

- **ejercicio3.py**  
  Convierte una cantidad de bytes ingresada por el usuario a kilobytes (KB), megabytes (MB) y gigabytes (GB) usando el sistema binario (1 KB = 1024 bytes).  
  👉 Los resultados se muestran con formato redondeado.

---

### 🛡️ Nivel Intermedio

- **ejercicio_intermedio.py**  
  Valida si una contraseña es segura. Verifica que tenga:
  - Al menos 8 caracteres  
  - Al menos un número  
  - Al menos una letra mayúscula  
  - Al menos un símbolo (como `!`, `@`, `#`, etc.)

  Además:
  - Usa `getpass` para que el usuario escriba la contraseña sin que se vea en pantalla  
  - Permite reintentar hasta que se ingrese una contraseña válida  

- **verificacion_servidores.py**  
  Simula la verificación de respuesta de varios servidores mediante "ping".  
  - Usa una lista de IPs  
  - Emplea `random.choice()` para simular si cada servidor responde o no  
  - Muestra resultados en consola con íconos visuales (`✅`, `❌`)  
  - La salida cambia cada vez que se ejecuta

---

### 💼 Nivel Avanzado

- **inventario_equipos.py**  
  Sistema de inventario de equipos informáticos con menú interactivo. Permite:
  - Agregar equipos (tipo, marca, modelo, número de serie y ubicación)
  - Buscar equipos por marca, tipo o ubicación
  - Ver estadísticas del inventario (por tipo y por ubicación)
  - Generar un informe completo con todos los equipos registrados

  👉 La información se almacena temporalmente en una lista de diccionarios. Todo se ejecuta desde un menú simple en consola, ideal para pruebas y formación técnica.

---
