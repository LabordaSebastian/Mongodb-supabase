import paho.mqtt.client as mqtt
import requests
import json

# Dirección del broker Mosquitto
BROKER = "localhost"
PORT = 1883
TOPIC = "iot/db"

# URL de la API FastAPI
API_URL = "http://localhost:8000/ciudades"

# Función para conectar al broker MQTT
def on_connect(client, userdata, flags, rc):
    print("Conectado al broker MQTT con código:", rc)
    print("Puede publicar opciones ahora.")
    
# Función para publicar mensajes en el topic MQTT
def publish_message(client, message):
    client.publish(TOPIC, message)
    print(f"Mensaje publicado en {TOPIC}: {message}")

# Función para obtener todas las ciudades desde la API
def get_ciudades():
    response = requests.get(API_URL)
    if response.status_code == 200:
        ciudades = response.json()
        for ciudad in ciudades:
            print(f"{ciudad['nombre']} - {ciudad['pais']} - Población: {ciudad['poblacion']} - Continente: {ciudad['continente']}")
    else:
        print("Error al obtener las ciudades desde la API.")

# Función para agregar una ciudad a través de la API
def agregar_ciudad():
    nombre = input("Ingrese el nombre de la ciudad: ")
    pais = input("Ingrese el país de la ciudad: ")
    poblacion = int(input("Ingrese la población de la ciudad: "))
    continente = input("Ingrese el continente de la ciudad: ")

    # Datos a enviar
    ciudad_data = {
        "nombre": nombre,
        "pais": pais,
        "poblacion": poblacion,
        "continente": continente
    }
    
    response = requests.post(API_URL, json=ciudad_data)
    if response.status_code == 200:
        print("Ciudad agregada correctamente.")
    else:
        print("Error al agregar la ciudad.")

# Función principal para el menú interactivo
def menu():
    client = mqtt.Client()
    client.on_connect = on_connect

    # Conectar al broker MQTT
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    while True:
        print("\nOpciones disponibles:")
        print("1. Ver todas las ciudades")
        print("2. Agregar una nueva ciudad")
        print("3. Publicar mensaje a MQTT")
        print("4. Salir")

        choice = input("Elija una opción: ")

        if choice == '1':
            get_ciudades()
        elif choice == '2':
            agregar_ciudad()
        elif choice == '3':
            message = input("Ingrese el mensaje a publicar: ")
            publish_message(client, message)
        elif choice == '4':
            print("Saliendo...")
            client.loop_stop()
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
