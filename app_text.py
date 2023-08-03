import streamlit as st
import pandas as pd
from datetime import datetime

# Creazione di dati di esempio
data = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
df = pd.DataFrame({"DATA": data, "VALORE": range(len(data))})

# Titolo dell'app
st.title("Seleziona un intervallo temporale")

# Interfaccia per selezionare l'intervallo
start_date_str = st.date_input("Seleziona la data di inizio", df['DATA'].min())
end_date_str = st.date_input("Seleziona la data di fine", df['DATA'].max())

# Conversione delle date in oggetti datetime
start_date = start_date_str
end_date = end_date_str

# Filtraggio dei dati in base all'intervallo selezionato
filtered_data = df[(df['DATA'] >= start_date) & (df['DATA'] <= end_date)]

# Visualizzazione dei dati filtrati
st.write("Dati nell'intervallo selezionato:")
st.dataframe(filtered_data)
