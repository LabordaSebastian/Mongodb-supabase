import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Cargar variables de entorno
load_dotenv()

# Configuración de Supabase
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_ANON_KEY')

# Crear cliente de Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY) 