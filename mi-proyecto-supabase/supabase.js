import { createClient } from '@supabase/supabase-js'
import * as dotenv from 'dotenv'
import { fileURLToPath } from 'url'
import { dirname } from 'path'
import path from 'path'

const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)
const envPath = path.resolve(__dirname, '.env')

// Cargar variables de entorno con verificación
const result = dotenv.config({ path: envPath })
if (result.error) {
    console.error('Error loading .env:', result.error)
    process.exit(1)
}

// Debug values before creating client
const supabaseUrl = process.env.SUPABASE_URL
const supabaseKey = process.env.SUPABASE_ANON_KEY

console.log('Debug Info:')
console.log('ENV Path:', envPath)
console.log('SUPABASE_URL:', supabaseUrl)
console.log('SUPABASE_KEY exists:', !!supabaseKey)
console.log('Raw SUPABASE_URL value:', JSON.stringify(supabaseUrl))

if (!supabaseUrl || !supabaseKey) {
    throw new Error(`Variables de entorno faltantes:
    SUPABASE_URL: ${!!supabaseUrl}
    SUPABASE_ANON_KEY: ${!!supabaseKey}
    Archivo .env en: ${envPath}`)
}

// Create and export client with explicit type conversion
export const supabase = createClient(String(supabaseUrl), String(supabaseKey))