# appel API de la route /patients/
# filtrage des données (genre, AVC, âge max) avec des widgets
# affichage du dataframe des données
# → Attention, l’API définie dans la 1ère partie doit bien être lancée en local pour avoir accès à la route.

import streamlit as st
import requests
import pandas as pd

URL = 'http://0.0.0.0:8000/patients'

def fetch_data(gender, stroke, max_age):
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

st.write('# Données')
st.write("Nous vous présentons des données issues du dataset Kaggle Healthcare Stroke Data. Vous pouvez explorer ces informations et utiliser différents paramètres pour filtrer les patients selon vos besoins.")

st.write('## Filtrer les données')
options = {
    'gender': {
        None: 'Aucun filtre',
        'male': 'Homme',
        'female': 'Femme',
        'other': 'Autre'
    },
    'stroke': {
        0: 'non',
        1: 'oui'
    }
}
col1, col2, col3 = st.columns(3)
gender = col1.selectbox('Genre', [i for i in options.get('gender')], accept_new_options=False, format_func=lambda x:  options.get('gender').get(x))
stroke = col2.segmented_control('Personnes ayant eu un AVC', [i for i in options.get('stroke')], width='stretch', format_func=lambda x:  options.get('stroke').get(x))
max_age = col3.number_input('Age maximum', step=1, min_value=0)
# st.write(f'gender: {gender}, stroke: {stroke}, max_age: {max_age}')

st.write('## Affichage du dataframe')

data = fetch_data(gender, stroke, max_age)
st.dataframe(data)