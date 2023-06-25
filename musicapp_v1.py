import streamlit as st
import pandas as pd

# Definir las tonalidades en bemoles
tonalidades = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

# Definir las notas en la escala mayor para cada tonalidad en bemoles
escalas = {
    "C": ["C7", "D7", "Dm7", "Dm7-G7", "E7", "F7", "G7", "Gm7-C7", "A7", "Am7-D7", "B7", "F7-G7"],
    "Db": ["Db7", "Eb7", "Ebm7", "Ebm7-Ab7", "F7", "Gb7", "Ab7", "Amb7-Db7" "Bb7", "Bbm7-Eb7", "C7", "Gb7-Ab7"],
    "D": ["D7", "E7", "Em7", "Em7-A7","F#7", "G7", "A7", "Am7-D7", "B7",  "Bm7-E7", "Db7", "G7-A7"],
    "Eb": ["Eb7", "F7", "Fm7", "Fm7-Bb7","G7", "Ab7", "Bb7", "Bbm7-E7", "C7", "Cm7-F7", "D7", "Ab7-Bb7"],
    "E": ["E7", "F#7", "F#m7", "F#m7-B7", "G#7", "A7", "B7", "Bm7-C7", "C#7", "C#m7-F#7", "D#7", "A7-B7"],
    "F": ["F7", "G7", "Gm7", "Gm7-C7","A7", "Bb7", "C7", "Cm7-F7",  "D7", "Dm7-G7", "E7", "Bb7-C7"],
    "Gb": ["Gb7", "Ab7", "ABm7", "Abm7-Db7",  "Bb7", "Cb7", "Db7", "Dbm7-Gb7", "Eb7", "Ebm7-Ab7", "F7", "Cb7-Db7"],
    "G": ["G7", "A7", "Am7", "Am7-D7", "B7", "C7", "D7", "Dm7-G7", "E7", "Em7-A7", "F#7", "C7-D7"],
    "Ab": ["Ab7", "Bb7", "Bbm7", "Bbm7-Eb7", "C7",  "Db7", "Eb7", "Ebm7-Ab7", "F7", "Fm7-Bb7" "G7", "Db7-Eb7"],
    "A": ["A7", "B7", "Bm7", "Bm7-E7", "C#7", "D7", "E7",  "Em7-A7","F#7", "F#m7-B7", "G#7", "D7-E7"],
    "Bb": ["Bb7", "C7", "Cm7", "Cm7-F7", "D7", "Eb7", "F7", "Fm7-Bb7", "G7", "Gm7-C7", "A7", "Eb-F7"],
    "B": ["B7", "C#7", "C#m7", "C#m7-F#7", "D#7", "E7", "F#7", "F#m7-B7","G#7", "G#m7-C#7", "A#7", "E7-F#7"],
}

# Definir los grados en las progresiones de blues
grados = {
    "I": 0,
    "II": 1,
    "IIm7": 2,
    "IIm7-V7":3,
    "V7/II": 8,
    "III": 4,
    "IV": 5, 
    "V": 6,
    "V7/V":1,
    "(IIm - V)/IV": 7,
    "(IIm - V)/V": 9,
    "IV-V":11
}

# Definir las progresiones
progresiones = {
    "Basic blues scale": [["I", "I", "I", "I"], ["IV", "IV", "I", "I"], ["V", "IV", "I", "I"]],
    "Dominant ending": [["I", "I", "I", "I"], ["IV", "IV", "I", "I"], ["V", "IV", "I", "V"]],
    "Traditional standard": [["I", "IV", "I", "I"], ["IV", "IV", "I", "I"], ["V", "IV", "I", "V"]],
    "Traditional II-V-I in bar 3": [["I", "IV", "I", "I"], ["IV", "IV", "I", "I"], ["IIm7", "V", "I", "V"]],
    "Double II-V-I": [["I", "IV", "I", "I"], ["IV", "IV", "I", "I"], ["IIm7", "V", "I", "IIm7-V7"]],
    "Jazz type blues": [["I", "IV", "I", "I"], ["IV", "IV", "I", "V7/II"], ["IIm7", "V", "I", "IIm7-V7"]],
    "Jazz type blues II": [["I", "IV", "I", "(IIm - V)/IV"], ["IV", "IIm7-V7", "I", "V7/II"], ["IIm7", "V", "I", "IIm7-V7"]],
    "Jazz type blues with dominant chain": [["I", "IV", "(IIm - V)/V", "(IIm - V)/IV"], ["IV", "IIm7-V7", "I", "V7/II"], ["V7/V", "V", "I", "IIm7-V7"]],
}

# Encabezado
st.title("Interactive Blues Progression App")

# Instrucciones
st.markdown("""
1. **Select a Key**: Choose a key from the dropdown menu. This is the musical key in which your blues progression will be played.
2. **Select a Progression**: Choose a chord progression from the dropdown menu. This will determine the structure of your blues progression. Various types of blues and jazz progressions are available to choose from.
3. **View Progression**: Once you have selected a key and a progression, the app will display your progression in both roman numerals and corresponding notes.

Feel free to use this music tool to explore and experiment with different chord progressions in various keys!
""")

# Crear la selección desplegable para las tonalidades
tonalidad_seleccionada = st.selectbox('Select a key:', tonalidades)

# Crear la selección desplegable para las progresiones
opcion_seleccionada = st.selectbox('Select a progression:', list(progresiones.keys()))

# Obtener la progresión seleccionada
progresion_seleccionada = progresiones[opcion_seleccionada]

# Transponer la progresión a la tonalidad seleccionada
progresion_transpuesta = [[escalas[tonalidad_seleccionada][grados[acorde]] for acorde in fila] for fila in progresion_seleccionada]




# Crear un dataframe para las notas
df_notas = pd.DataFrame(progresion_transpuesta)

# Convertir el DataFrame a HTML sin índices ni encabezados
df_notas_html = df_notas.to_html(index=False, header=False)

# Usar CSS para personalizar el ancho de las columnas
df_notas_styled = f'<style>.dataframe th {{width: 120px;}}</style>{df_notas_html}'

st.write("Chord Progression:")

# Mostrar el DataFrame en Streamlit
st.markdown(df_notas_styled, unsafe_allow_html=True)

# Agregar una línea en blanco para separar los dos dataframes
st.write("")

# Crear un dataframe para la progresión en numeración romana
df_grados = pd.DataFrame(progresion_seleccionada)

# Convertir el DataFrame a HTML sin índices ni encabezados
df_grados_html = df_grados.to_html(index=False, header=False)

st.write("Numeral Progression:")

# Mostrar el DataFrame en Streamlit
st.markdown(df_grados_html, unsafe_allow_html=True)

# Agregar una línea en blanco para separar los dos dataframes
st.write("")

# Agregar una línea en blanco para separar los dos dataframes
st.write("")

# Agregar una línea en blanco para separar los dos dataframes
st.write("")
st.markdown("""
Raul Camara 2023
""")