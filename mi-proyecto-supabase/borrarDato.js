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