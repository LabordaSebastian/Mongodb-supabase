import { supabase } from './supabase.js'

async function verRegistros() {
  try {
    console.log('Consultando datos...')
    
    // Consulta con filtros y ordenamiento
    const { data, error } = await supabase
      .from('Base_datos_ejemplo')
      .select('*')
      .order('Season', { ascending: true })
      .limit(10)
    
    if (error) {
      console.error('Error al consultar datos:', error)
      return
    }
    
    if (!data || data.length === 0) {
      console.log('No hay registros en la tabla')
      return
    }
    
    // Mostrar estadísticas básicas
    console.log('\nEstadísticas:')
    const seasons = [...new Set(data.map(d => d.Season))]
    const competitions = [...new Set(data.map(d => d.Competition))]
    
    console.log('Temporadas:', seasons)
    console.log('Competiciones:', competitions)
    console.log('Total de registros:', data.length)
    
    // Mostrar datos formateados
    console.log('\nÚltimos 10 registros:')
    const formattedData = data.map(d => ({
      Temporada: d.Season,
      Competición: d.Competition,
      Fecha: d.Date,
      Club: d.Club,
      Resultado: d.Result,
      Tipo: d.Type || 'N/A'
    }))
    
    console.table(formattedData)
  } catch (err) {
    console.error('Error:', err)
  }
}

verRegistros()