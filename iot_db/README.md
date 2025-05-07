🔧 1. Diseño General del Sistema
Componentes:
MongoDB: Base de datos que almacena la información de las 20 ciudades.

REST API (Flask o FastAPI): Intermediaria entre MQTT y MongoDB. Lee y escribe en la base de datos.

Mosquitto: Broker MQTT.

Publisher MQTT: Cliente que publica mensajes solicitando o modificando datos.

Subscriber MQTT (la API): La API suscribe a los temas y responde con acciones sobre la base de datos.

🗂 2. Diseño de la Base de Datos
Se genera el archivo ciudades.json, base de datos que contiene las 20 ciudades más grandes del mundo.
{
  "nombre": "Buenos Aires",
  "pais": "Argentina",
  "poblacion": 2890000,
  "continente": "Sudamérica"
}


🖥 3. Configuración de MongoDB
Instalación de MongoDB local e inicio
Se sigue el tutorial de instalación en Ubuntu
https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/

Creación de la base de datos
- Abrir la shell de mongoDB:
mongosh
- Crear la base de datos y la coleccion "ciudades":
use iot_db
db.createCollection("ciudades")
show collections # Verificar que se creó la colección

- Salir del shell e importar la base de datos:
exit
mongoimport --db iot_db --collection ciudades --file ciudades.json --jsonArray

🌐 4. Creación de la API para consultar y modificar datos en MongoDB (Python + FastAPI recomendado)
Estructura de la API:
api/
├── main.py
└── requirements.txt

- Se usa un entorno virtual para no instalar paquetes globales.
# 1. Crear entorno virtual
python3 -m venv venv

# 2. Activarlo
source venv/bin/activate  # Linux/macOS
# o
venv\Scripts\activate     # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar FastAPI
uvicorn main:app --reload

✅ Verificar que la API está funcionando
- Probá la API en tu navegador o con curl
📌 En el navegador:
Abrí http://localhost:8000/docs
Deberías ver la interfaz Swagger, y ahí podés:
Hacer un GET /ciudades
Hacer un POST para agregar una ciudad
Etc.

🧪 O con curl (línea de comandos):
curl http://localhost:8000/ciudades

📡 5. Mosquitto MQTT Broker
- Correr el broker fácilmente usando Docker.

✅ 1. Crear la estructura de configuración local
Primero, crea un directorio con subdirectorios:
mkdir -p ~/mosquitto/config
mkdir -p ~/mosquitto/data
mkdir -p ~/mosquitto/log

✅ 2. Crear un archivo de configuración mínimo
Edita el archivo mosquitto.conf:
nano config/mosquitto.conf

persistence true
persistence_location /mosquitto/data/
log_dest file /mosquitto/log/mosquitto.log
listener 1883
allow_anonymous true

✅ 3. Levantar el contenedor con Docker
Ahora ejecuta este comando:
docker run -it --name mosquitto -p 1883:1883 -v "$PWD/mosquitto/config:/mosquitto/config" -v /mosquitto/data -v /mosquitto/log eclipse-mosquitto

