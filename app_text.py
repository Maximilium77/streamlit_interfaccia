import streamlit as st
import pandas as pd
from datetime import datetime

import subprocess

module_name = "openpyxl"

# Esegui il comando di installazione utilizzando pip
try:
    subprocess.check_call(["pip", "install", module_name])
    print(f"Modulo {module_name} installato con successo.")
except subprocess.CalledProcessError:
    print(f"Si è verificato un errore durante l'installazione di {module_name}.")


# Upload del file Excel
uploaded_file = st.file_uploader("Carica un file Excel", type=["xlsx"])

if uploaded_file is not None:
    # Leggi il file Excel e crea il DataFrame
    df = pd.read_excel(uploaded_file)


# Creazione di dati di esempio
data = pd.date_range(start="2023-01-01", end="2023-01-31", freq="D")
df = pd.DataFrame({"DATA": data, "VALORE": range(len(data))})

# Titolo dell'app
st.title("App con selezione intervallo temporale e upload di un file Excel")

# Interfaccia per selezionare l'intervallo
start_date = st.date_input("Seleziona la data di inizio", df['DATA'].min())
end_date = st.date_input("Seleziona la data di fine", df['DATA'].max())

# Filtraggio dei dati in base all'intervallo selezionato
filtered_data = df[(df['DATA'] >= pd.to_datetime(start_date)) & (df['DATA'] <= pd.to_datetime(end_date))]

# Visualizzazione dei dati filtrati
st.write("Dati nell'intervallo selezionato:")
st.dataframe(filtered_data)
