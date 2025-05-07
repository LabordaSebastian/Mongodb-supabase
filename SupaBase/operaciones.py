from db_config import supabase

def insertar_registro(tabla: str, datos: dict):
    """
    Inserta un nuevo registro en la tabla especificada.
    
    Args:
        tabla (str): Nombre de la tabla
        datos (dict): Diccionario con los datos a insertar
        
    Returns:
        dict: Registro insertado o None si hay error
    """
    try:
        response = supabase.table(tabla).insert(datos).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Error al insertar en la tabla {tabla}: {str(e)}")
        return None

def actualizar_registro(tabla: str, id: int, datos: dict):
    """
    Actualiza un registro existente.
    
    Args:
        tabla (str): Nombre de la tabla
        id (int): ID del registro a actualizar
        datos (dict): Diccionario con los datos a actualizar
        
    Returns:
        dict: Registro actualizado o None si hay error
    """
    try:
        response = supabase.table(tabla).update(datos).eq("id", id).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Error al actualizar el registro {id} en la tabla {tabla}: {str(e)}")
        return None

def eliminar_registro(tabla: str, id_paciente: int):
    """
    Elimina un registro específico.
    
    Args:
        tabla (str): Nombre de la tabla
        id_paciente (int): ID del paciente del registro a eliminar
        
    Returns:
        bool: True si se eliminó correctamente, False en caso contrario
    """
    try:
        response = supabase.table(tabla).delete().eq("id_paciente", id_paciente).execute()
        return True if response.data else False
    except Exception as e:
        print(f"Error al eliminar el registro {id_paciente} en la tabla {tabla}: {str(e)}")
        return False

def obtener_campos_y_plantilla(tabla):
    if tabla == "Clinica1":
        campos = [
            "nombre_paciente",
            "edad",
            "genero",
            "telefono",
            "email",
            "alergias",
            "historial_medico"
        ]
        ejemplo = {
            "nombre_paciente": "Ej: Juan Pérez",
            "edad": "Ej: 42",
            "genero": "Ej: Masculino",
            "telefono": "Ej: 555-5678",
            "email": "Ej: juan@email.com",
            "alergias": "Ej: Ninguna",
            "historial_medico": "Ej: Diabetes tipo 2"
        }
        return campos, ejemplo
    elif tabla == "Citas":
        campos = [
            "nombre_doctor",
            "especialidad",
            "fecha_cita",
            "diagnostico",
            "tratamiento"
        ]
        ejemplo = {
            "nombre_doctor": "Ej: Dr. Carlos Méndez",
            "especialidad": "Ej: Cardiología",
            "fecha_cita": "Ej: 2023-10-15",
            "diagnostico": "Ej: Presión arterial elevada",
            "tratamiento": "Ej: Dieta baja en sodio y ejercicio"
        }
        return campos, ejemplo
    else:
        return [], {}

def main():
    print("\n=== OPERACIONES DE BASE DE DATOS ===")
    tabla = input("Ingrese el nombre de la tabla (Ej: Clinica1 o Citas): ").strip()
    
    print("\nOpciones disponibles:")
    print("1. Insertar nuevo registro")
    print("2. Eliminar registro")
    
    opcion = input("\nSeleccione una opción (1-2): ")
    
    if opcion == "1":
        print(f"\n=== INSERTAR NUEVO REGISTRO EN {tabla.upper()} ===")
        campos, ejemplo = obtener_campos_y_plantilla(tabla)
        datos = {}
        if campos:
            print("\nPor favor, complete los siguientes campos:")
            for campo in campos:
                valor = input(f"{campo} ({ejemplo[campo]}): ")
                datos[campo] = valor
            resultado = insertar_registro(tabla, datos)
            if resultado:
                print("\nRegistro insertado exitosamente:")
                print(resultado)
            else:
                print("\nError al insertar el registro")
        else:
            print("\nTabla no reconocida o sin plantilla definida. Inserción manual.")
            while True:
                campo = input("\nIngrese el nombre del campo (o 'fin' para terminar): ")
                if campo.lower() == 'fin':
                    break
                valor = input(f"Ingrese el valor para {campo}: ")
                datos[campo] = valor
            if datos:
                resultado = insertar_registro(tabla, datos)
                if resultado:
                    print("\nRegistro insertado exitosamente:")
                    print(resultado)
                else:
                    print("\nError al insertar el registro")
    elif opcion == "2":
        print("\n=== ELIMINAR REGISTRO ===")
        id_paciente = input("Ingrese el valor de id_paciente del registro a eliminar: ")
        if not id_paciente.isdigit():
            print("ID inválido. Debe ser un número.")
        elif eliminar_registro(tabla, int(id_paciente)):
            print(f"\nRegistro con id_paciente {id_paciente} eliminado exitosamente")
        else:
            print(f"\nError al eliminar el registro con id_paciente {id_paciente}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main() 