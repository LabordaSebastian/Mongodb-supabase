import { supabase } from './supabase.js'

async function insertarDato() {
  try {
    console.log('Insertando nuevo registro...')
    
    const { data, error } = await supabase
      .from('Base_datos_ejemplo')
      .insert([
        {
          Season: '23/24',
          Competition: 'Liga Argentina',
          Matchday: '1',
          Date: '2024-05-07',
          Venue: 'H',
          Club: 'Coassolo FC',
          Opponent: 'River Plate',
          Result: '3:0',
          Playing_Position: 'ST',
          Minute: '90',
          At_score: '3:0',
          Type: 'Gol de cabeza',
          Goal_assist: 'Messi'
        }
      ])
      .select()

    if (error) {
      console.error('Error al insertar:', error)
      return
    }

    console.log('Dato insertado correctamente:', data)
  } catch (err) {
    console.error('Error:', err)
  }
}

insertarDato()