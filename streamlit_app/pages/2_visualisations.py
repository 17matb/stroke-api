# Graphiques interactifs (Plotly) : deux graphes de votre choix qui fournissent des informations pertinentes sur les données.
# Ajouter de quelques phrases pour commenter les graphes

import streamlit as st
import plotly.express as px
import requests
import pandas as pd

URL = 'http://0.0.0.0:8000/patients'

def fetch_data(gender = None, stroke = None, max_age = None):
    try:
        params = {
            'gender': gender,
            'stroke': stroke,
            'max_age': max_age
        }
        response = requests.get(URL, params)
        fetched_data = response.json()
        df = pd.DataFrame(fetched_data)
        return df
    except Exception as e:
        print(f'error: {e}')

data = fetch_data()
patients_that_had_a_stroke = data.loc[data['stroke'] == 1]
patients_no_stroke = data.loc[data['stroke'] == 0]

st.write('# Visualisations')
st.write('## Répartitions de l\'IMC et du taux de glucose moyen chez les patients ayant eu un AVC')
fig = px.scatter(patients_that_had_a_stroke, x='avg_glucose_level', y='bmi', labels={'bmi': 'IMC', 'avg_glucose_level': 'Taux de glucose moyen'})
st.plotly_chart(fig)
st.write('Ce graphique nous montre une dispersion assez large ce qui laisse penser que l\'IMC et le taux de glucose moyen ne sont pas des facteurs très déterminants pour prédire un AVC.')
st.write('## Répartition du genre chez les patients')
col1, col2 = st.columns(2)
fig2 = px.pie(patients_that_had_a_stroke, names='gender', title='Patients ayant eu un AVC', hole=0.5)
fig2_bis = px.pie(patients_no_stroke, names='gender', title='Patients n\'ayant pas eu un AVC', hole=0.5)
col1.plotly_chart(fig2)
col2.plotly_chart(fig2_bis)
st.write('Ici, nos deux répartitions de genre entre patients ayant eu un AVC et ceux n\'en n\'ayant pas eu sont quasi identiques. Cela nous montre que le genre n\'est pas non plus un facteur important pour une prédiction.')