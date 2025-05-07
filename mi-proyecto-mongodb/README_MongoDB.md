
# README - MongoDB Básico

Este archivo contiene una descripción completa de MongoDB, así como una guía paso a paso para levantar un entorno en Xubuntu, probar su funcionamiento, ejecutar operaciones básicas y acceder a una base de datos mediante un script Python.

---

## ¿Qué es MongoDB?

MongoDB es una base de datos NoSQL orientada a documentos, de código abierto, diseñada para almacenar grandes volúmenes de datos de manera flexible, escalable y de alto rendimiento. En lugar de almacenar datos en tablas como en las bases de datos relacionales (SQL), MongoDB utiliza documentos en formato BSON (una versión binaria de JSON), que permiten representar estructuras de datos complejas y anidadas.

### Características clave de MongoDB

- **Modelo de documentos (document-based)**: Los datos se almacenan en estructuras llamadas documentos, parecidas a objetos JSON. Cada documento puede tener una estructura diferente, lo que ofrece flexibilidad en el esquema.
- **Esquema flexible (schema-less)**: No requiere una definición fija de estructura antes de insertar datos. Ideal para aplicaciones donde el esquema cambia con frecuencia.
- **Escalabilidad horizontal**: A través de sharding, permite dividir datos en múltiples servidores.
- **Alta disponibilidad**: Usa replica sets para recuperación automática ante fallos.
- **Consultas poderosas**: Basadas en JSON, permiten filtrado, ordenamiento, agregación, búsqueda de texto, etc.
- **Índices**: Mejora el rendimiento de consultas.
- **Agregación**: Framework de procesamiento de datos similar a GROUP BY en SQL.

### Usos comunes

Ideal para:
- Grandes volúmenes de datos con estructuras cambiantes.
- Datos jerárquicos o anidados.
- Aplicaciones móviles, IoT, tiempo real, catálogos, CMS.

### Comparación con bases de datos relacionales

| Característica      | MongoDB                    | Bases de Datos Relacionales |
|---------------------|----------------------------|-----------------------------|
| Modelo de datos     | Documentos BSON (tipo JSON) | Tablas y filas              |
| Esquema             | Flexible                   | Fijo                        |
| Joins               | Limitados                  | Amplio soporte              |
| Escalabilidad       | Horizontal (sharding)      | Mayormente vertical         |
| Transacciones       | Soporte desde v4.0         | Soporte completo            |
| Rendimiento         | Alta velocidad             | Variable                    |


### Ventajas

- Esquema flexible, buen rendimiento, fácil de escalar, gran comunidad.

### Desventajas

- No ideal para transacciones complejas, mayor uso de espacio, esquema sin control puede causar desorden.

---

## Instalación en Xubuntu

```bash
sudo apt update
sudo apt install -y mongodb
sudo systemctl start mongodb
sudo systemctl enable mongodb
sudo systemctl status mongodb
```
---

## Probar funcionamiento con `mongosh`

```bash
mongosh
```

```js
use miapp
db.usuarios.insertOne({ nombre: "Maxi", edad: 30 })
db.usuarios.find()
```

---

## Comandos útiles

```js
// Insertar múltiples
db.usuarios.insertMany([
  { nombre: "Ana", edad: 25 },
  { nombre: "Luis", edad: 35, domicilio: "Calle Falsa 123" },
  { nombre: "Lucía", edad: 28 }
])

// Buscar por campo
db.usuarios.find({ edad: 25 })

// Eliminar uno por campo
db.usuarios.deleteOne({ nombre: "Ana" })

// Eliminar todos
db.usuarios.deleteMany({})

// Eliminar colección
db.usuarios.drop()

// Eliminar base de datos
db.dropDatabase()

// Listar bases
show dbs
```

### Insertar con esquema flexible

```js
db.usuarios.insertOne({ nombre: "Carlos", edad: 40, domicilio: "Av. Siempre Viva" })
```

---

## Conectar desde Python

```bash
python3 -m venv venv
source venv/bin/activate
pip install pymongo
```


## 🧾 Script interactivo

`menu_usuarios.py`:

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["base-ejemplo"]
coleccion = db["usuarios"]

def mostrar_usuarios():
    usuarios = list(coleccion.find())
    if usuarios:
        print("
📋 Lista de usuarios:")
        for u in usuarios:
            print(f"- {u}")
    else:
        print("
⚠️ No hay usuarios en la base de datos.")

def agregar_usuario():
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    correo = input("Ingrese el correo: ")
    domicilio = input("Ingrese el domicilio (opcional): ")

    usuario = { "nombre": nombre, "edad": int(edad), "correo": correo }
    if domicilio:
        usuario["domicilio"] = domicilio

    coleccion.insert_one(usuario)
    print("✅ Usuario agregado con éxito.")

def eliminar_usuario():
    nombre = input("Ingrese el nombre del usuario a eliminar: ")
    resultado = coleccion.delete_one({"nombre": nombre})
    if resultado.deleted_count > 0:
        print("🗑️ Usuario eliminado correctamente.")
    else:
        print("❌ Usuario no encontrado.")

def menu():
    while True:
        print("
🧾 Menú de opciones:")
        print("1 - Mostrar usuarios")
        print("2 - Agregar usuario")
        print("3 - Eliminar usuario")
        print("4 - Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_usuarios()
        elif opcion == "2":
            agregar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            print("👋 Saliendo...")
            break
        else:
            print("❗ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
```

---

Este proyecto permite levantar y gestionar una base de datos MongoDB desde consola y desde Python de manera sencilla y extensible. Ideal para pruebas, prototipos y enseñanza.
