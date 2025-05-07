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