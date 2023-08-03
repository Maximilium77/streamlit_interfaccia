import streamlit as st
import pandas as pd
from datetime import datetime

# Titolo dell'app
st.title("App con selezione intervallo temporale e upload di un file Excel")

# Upload del file Excel
uploaded_file = st.file_uploader("Carica un file Excel", type=["xlsx"])

if uploaded_file is not None:
    # Leggi il file Excel e crea il DataFrame
    df = pd.read_excel(uploaded_file)

    # Interfaccia per selezionare l'intervallo
    start_date = st.date_input("Seleziona la data di inizio", df['DATA'].min())
    end_date = st.date_input("Seleziona la data di fine", df['DATA'].max())

    # Filtraggio dei dati in base all'intervallo selezionato
    filtered_data = df[(df['DATA'] >= pd.to_datetime(start_date)) & (df['DATA'] <= pd.to_datetime(end_date))]

    # Visualizzazione dei dati filtrati
    st.write("Dati nell'intervallo selezionato:")
    st.dataframe(filtered_data)
