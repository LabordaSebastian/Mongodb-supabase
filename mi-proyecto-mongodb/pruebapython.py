from pymongo import MongoClient

# Conexión a MongoDB local
client = MongoClient("mongodb://localhost:27017/")
db = client["base-ejemplo"]
coleccion = db["usuarios"]

def mostrar_usuarios():
    usuarios = list(coleccion.find())
    if usuarios:
        print("\n📋 Lista de usuarios:")
        for u in usuarios:
            print(f"- {u}")
    else:
        print("\n⚠️ No hay usuarios en la base de datos.")

def agregar_usuario():
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    correo = input("Ingrese el correo: ")
    domicilio = input("Ingrese el domicilio (opcional, puede dejar vacío): ")

    usuario = {
        "nombre": nombre,
        "edad": int(edad),
        "correo": correo
    }

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
        print("\n🧾 Menú de opciones:")
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


