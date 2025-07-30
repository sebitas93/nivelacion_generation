import random  # Importamos la librería para generar respuestas aleatorias

# Lista de direcciones IP simuladas de servidores
import random
import time

random.seed(time.time())  # Usa la hora actual como base de aleatoriedad

ips_servidores = ["192.168.1.10", "10.0.0.5", "192.168.34.2", "172.16.0.3"]

for ip in ips_servidores:
    respuesta_ping = random.choice([True, False])
    if respuesta_ping:
        print(f" El servidor {ip} está respondiendo.")
    else:
        print(f" ¡Alerta! El servidor {ip} no responde.")

