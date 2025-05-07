from db_config import supabase
from tabulate import tabulate

def obtener_todos_los_registros(tabla: str):
    """
    Obtiene todos los registros de una tabla específica.
    
    Args:
        tabla (str): Nombre de la tabla a consultar
        
    Returns:
        list: Lista de registros encontrados
    """
    try:
        response = supabase.table(tabla).select("*").execute()
        return response.data
    except Exception as e:
        print(f"Error al consultar la tabla {tabla}: {str(e)}")
        return []

def obtener_registro_por_id(tabla: str, campo_id: str, id_valor):
    """
    Obtiene un registro específico por su ID.
    
    Args:
        tabla (str): Nombre de la tabla
        campo_id (str): Nombre del campo ID
        id_valor (any): Valor del ID a buscar
        
    Returns:
        dict: Registro encontrado o None si no existe
    """
    try:
        response = supabase.table(tabla).select("*").eq(campo_id, id_valor).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Error al consultar el registro {id_valor} en la tabla {tabla}: {str(e)}")
        return None

def buscar_registros(tabla: str, campo: str, valor: any):
    """
    Busca registros que coincidan con un valor específico en un campo.
    
    Args:
        tabla (str): Nombre de la tabla
        campo (str): Nombre del campo a buscar
        valor (any): Valor a buscar
        
    Returns:
        list: Lista de registros que coinciden con la búsqueda
    """
    try:
        response = supabase.table(tabla).select("*").eq(campo, valor).execute()
        return response.data
    except Exception as e:
        print(f"Error al buscar en la tabla {tabla}: {str(e)}")
        return []

def mostrar_tabla(registros):
    if not registros:
        print("\nNo hay registros para mostrar.")
        return
    print("\nRegistros encontrados:")
    print(tabulate(registros, headers="keys", tablefmt="grid", showindex=True))

def main():
    print("\n=== CONSULTA DE REGISTROS ===")
    tabla = input("Ingrese el nombre de la tabla a consultar: ")
    while True:
        print("\nOpciones de consulta:")
        print("1. Ver todos los registros")
        print("2. Buscar por ID")
        print("3. Buscar por campo específico")
        print("4. Salir")
        opcion = input("\nSeleccione una opción (1-4): ")
        if opcion == "1":
            registros = obtener_todos_los_registros(tabla)
            mostrar_tabla(registros)
        elif opcion == "2":
            campo_id = input("Ingrese el nombre del campo ID (por ejemplo, id_paciente): ")
            id_registro = input("Ingrese el valor del ID a buscar: ")
            if not id_registro.isdigit():
                print("ID inválido. Debe ser un número.")
                continue
            registro = obtener_registro_por_id(tabla, campo_id, int(id_registro))
            mostrar_tabla([registro] if registro else [])
        elif opcion == "3":
            campo = input("Ingrese el nombre del campo a buscar: ")
            valor = input("Ingrese el valor a buscar: ")
            registros = buscar_registros(tabla, campo, valor)
            mostrar_tabla(registros)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main() 