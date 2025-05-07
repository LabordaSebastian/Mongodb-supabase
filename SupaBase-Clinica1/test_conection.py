from db_config import supabase

print("Probando conexión y consulta...")
try:
    response = supabase.table("Clinica1").select("*").execute()
    print("Respuesta cruda:", response)
    print("Datos:", response.data)
except Exception as e:
    print("Error:", e)