# Supabase
Guia de como implementar un base de datos en supabase

## Supabase

Supabase es una alternativa de código abierto a Firebase, que proporciona una plataforma de desarrollo backend completa. Está construida sobre PostgreSQL y ofrece un conjunto de herramientas y servicios para crear aplicaciones escalables.

### ¿Cómo funciona?

Supabase combina varias tecnologías de código abierto para proporcionar funcionalidades de backend:

- **Base de datos PostgreSQL**: Motor principal de base de datos relacional
- **Autenticación**: Sistema integrado de manejo de usuarios
- **Almacenamiento**: Almacenamiento de archivos integrado con S3
- **API instantánea**: Generación automática de API REST y GraphQL
- **Funciones Edge**: Ejecución de funciones serverless
- **Actualizaciones en tiempo real**: Suscripciones en tiempo real mediante WebSockets

### Ventajas

- ✅ **Código abierto**: Completo control sobre tus datos y la infraestructura
- ✅ **SQL completo**: Acceso a todas las características de PostgreSQL
- ✅ **Escalabilidad**: Diseñado para manejar aplicaciones de gran escala
- ✅ **Auto-hospedaje**: Opción de hospedar en tu propia infraestructura
- ✅ **Dashboard intuitivo**: Interface gráfica para gestión de datos
- ✅ **Migración sencilla**: Compatibilidad con bases de datos existentes
- ✅ **Precio competitivo**: Tier gratuito generoso y precios escalables

### Desventajas

- ❌ **Curva de aprendizaje**: Requiere conocimiento de SQL para aprovechar todo su potencial
- ❌ **Menos servicios**: Comparado con Firebase, tiene menos servicios integrados
- ❌ **Comunidad más pequeña**: Ecosistema más reducido que alternativas como Firebase
- ❌ **Menos documentación**: Al ser más nuevo, tiene menos recursos y ejemplos
- ❌ **Limitaciones en tiempo real**: Las funcionalidades en tiempo real son más básicas que Firebase

# Guía de Configuración y Uso de Supabase con Node.js

## Requisitos Previos
- Node.js v18 o superior
- Una cuenta en Supabase
- npm (Node Package Manager)

## Paso 1: Crear el Proyecto
```bash
# Crear directorio del proyecto
mkdir mi-proyecto-supabase
cd mi-proyecto-supabase

# Inicializar proyecto Node.js
npm init -y

# Instalar dependencias necesarias
npm install @supabase/supabase-js dotenv
```

## Paso 2: Configurar Supabase
1. Ir a [app.supabase.com](https://app.supabase.com)
2. Crear nuevo proyecto
3. Guardar las credenciales:
   - URL del proyecto
   - anon/public key (¡NO la service_role key!)

## Paso 3: Configurar el Entorno
Crear archivo `.env`:
```properties
SUPABASE_URL=tu_url_de_supabase
SUPABASE_ANON_KEY=tu_anon_key
```

## Paso 4: Configurar Cliente Supabase
Crear archivo `supabase.js`:
```javascript
import { createClient } from '@supabase/supabase-js'
import * as dotenv from 'dotenv'
import { fileURLToPath } from 'url'
import { dirname } from 'path'
import path from 'path'

const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)
const envPath = path.resolve(__dirname, '.env')

const result = dotenv.config({ path: envPath })
if (result.error) {
    console.error('Error loading .env:', result.error)
    process.exit(1)
}

const supabaseUrl = process.env.SUPABASE_URL
const supabaseKey = process.env.SUPABASE_ANON_KEY

export const supabase = createClient(supabaseUrl, supabaseKey)
```

## Paso 5: Crear Tabla en Supabase
1. Ir al Dashboard de Supabase
2. Table Editor → New Table
3. Nombre: "Base_datos_ejemplo"
4. Columnas:
   - Season (text)
   - Competition (text)
   - Matchday (text)
   - Date (date)
   - Venue (text)
   - Club (text)
   - Opponent (text)
   - Result (text)
   - Playing_Position (text)
   - Minute (text)
   - At_score (text)
   - Type (text)
   - Goal_assist (text)

5. SQL para configurar columnas:
```sql
-- Ejecutar en SQL Editor
ALTER TABLE "Base_datos_ejemplo" ADD COLUMN IF NOT EXISTS "Season" text;
ALTER TABLE "Base_datos_ejemplo" ADD COLUMN IF NOT EXISTS "Competition" text;
ALTER TABLE "Base_datos_ejemplo" ADD COLUMN IF NOT EXISTS "Date" date;
ALTER TABLE "Base_datos_ejemplo" ADD COLUMN IF NOT EXISTS "Venue" text;
ALTER TABLE "Base_datos_ejemplo" ADD COLUMN IF NOT EXISTS "Club" text;
ALTER TABLE "Base_datos_ejemplo" ADD COLUMN IF NOT EXISTS "Opponent" text;
ALTER TABLE "Base_datos_ejemplo" ADD COLUMN IF NOT EXISTS "Result" text;
ALTER TABLE "Base_datos_ejemplo" ADD COLUMN IF NOT EXISTS "Playing_Position" text;
ALTER TABLE "Base_datos_ejemplo" ADD COLUMN IF NOT EXISTS "Minute" text;
ALTER TABLE "Base_datos_ejemplo" ADD COLUMN IF NOT EXISTS "Matchday" text;
ALTER TABLE "Base_datos_ejemplo" ADD COLUMN IF NOT EXISTS "At_score" text;
ALTER TABLE "Base_datos_ejemplo" ADD COLUMN IF NOT EXISTS "Type" text;
ALTER TABLE "Base_datos_ejemplo" ADD COLUMN IF NOT EXISTS "Goal_assist" text;
```

## Paso 6: Configurar RLS (Row Level Security)
En SQL Editor de Supabase:
```sql
-- Habilitar RLS
ALTER TABLE "Base_datos_ejemplo" ENABLE ROW LEVEL SECURITY;

-- Política para permitir lectura a todos los usuarios
CREATE POLICY "Allow select for all users" 
ON "public"."Base_datos_ejemplo"
FOR SELECT 
TO authenticated
USING (true);

-- Política para permitir inserción a todos los usuarios
CREATE POLICY "Allow insert for all users"
ON "public"."Base_datos_ejemplo"
FOR INSERT
TO authenticated
WITH CHECK (true);
```

## Paso 7: Scripts de Consulta
Crear archivo para ver registros (`verRegistros.js`):
```javascript
import { supabase } from './supabase.js'

async function verRegistros() {
  try {
    console.log('Consultando datos...')
    const { data, error } = await supabase
      .from('Base_datos_ejemplo')
      .select('*')
      .order('Season', { ascending: true })
      .limit(10)
    
    if (error) {
      console.error('Error:', error)
      return
    }
    
    console.log('Registros encontrados:', data.length)
    console.table(data)
  } catch (err) {
    console.error('Error:', err)
  }
}

verRegistros()
```

## Paso 8: Script para Insertar Datos
Crear archivo para insertar registros (`insertarDato.js`):
```javascript
import { supabase } from './supabase.js'

async function insertarDato() {
  try {
    const { data, error } = await supabase
      .from('Base_datos_ejemplo')
      .insert([
        {
          Season: '23/24',
          Competition: 'Liga Argentina',
          Matchday: '1',
          Date: '2024-05-07',
          Venue: 'H',
          Club: 'Ejemplo FC',
          Opponent: 'Rival FC',
          Result: '3:0',
          Playing_Position: 'ST',
          Minute: '90',
          At_score: '3:0',
          Type: 'Header',
          Goal_assist: 'Asistidor'
        }
      ])
      .select()

    if (error) throw error
    console.log('Dato insertado:', data)
  } catch (err) {
    console.error('Error:', err)
  }
}

insertarDato()
```

## Paso 9: Script para Buscar Datos
Crear archivo para buscar registros (`buscarDato.js`):
```javascript
import { supabase } from './supabase.js'

async function buscarDato() {
  try {
    console.log('Buscando dato específico...')
    
    const { data, error } = await supabase
      .from('Base_datos_ejemplo')
      .select('*')
      .eq('Season', '23/24')
      .eq('Competition', 'Liga Argentina')
      .eq('Club', 'Coassolo FC')
      .eq('Date', '2024-05-07')
      .eq('Opponent', 'River Plate')
      .single()

    if (error) {
      console.error('Error al buscar:', error)
      return
    }

    if (data) {
      console.log('Registro encontrado:')
      console.table(data)
    } else {
      console.log('No se encontró el registro')
    }

  } catch (err) {
    console.error('Error:', err)
  }
}

buscarDato()
```

## Paso 10: Script para Borrar Datos
Crear archivo para borrar registros (`borrarDato.js`):
```javascript
import { supabase } from './supabase.js'

async function borrarDato() {
  try {
    console.log('Intentando borrar dato específico...')
    
    const { data, error } = await supabase
      .from('Base_datos_ejemplo')
      .delete()
      .eq('Season', '23/24')
      .eq('Competition', 'Liga Argentina')
      .eq('Club', 'Coassolo FC')
      .eq('Date', '2024-05-07')
      .eq('Opponent', 'River Plate')
      .select()

    if (error) {
      console.error('Error al borrar:', error)
      return
    }

    if (data && data.length > 0) {
      console.log('Registro(s) eliminado(s):')
      console.table(data)
      console.log('✅ Eliminación exitosa')
    } else {
      console.log('❌ No se encontró el registro para eliminar')
    }

  } catch (err) {
    console.error('Error:', err)
  }
}

borrarDato()
```

## Uso
```bash
# Ver registros
node verRegistros.js

# Insertar nuevo registro
node insertarDato.js

# Buscar registro específico
node buscarDato.js

# Borrar registro específico
node borrarDato.js
```

## Solución de Problemas Comunes
1. **Error "supabaseUrl is required"**
   - Verificar archivo `.env`
   - Verificar que dotenv esté cargando correctamente

2. **Error "RLS"**
   - Verificar políticas de seguridad en Supabase
   - Configurar RLS correctamente

3. **No se encuentran registros**
   - Verificar que la tabla exista
   - Verificar que haya datos importados
   - Verificar permisos RLS

## Notas Importantes
- Nunca compartir la `service_role` key
- Mantener el archivo `.env` en `.gitignore`
- Usar siempre la `anon` key para conexiones desde el cliente
- Las políticas RLS deben configurarse adecuadamente para permitir las operaciones necesarias
