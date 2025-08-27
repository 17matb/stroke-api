# appel API de la route /patients/
# filtrage des données (genre, AVC, âge max) avec des widgets
# affichage du dataframe des données
# → Attention, l’API définie dans la 1ère partie doit bien être lancée en local pour avoir accès à la route.

import streamlit as st
from streamlit_app.fetch_api import fetch_data

st.write('# Données')
st.write(
    'Voici des données issues du dataset Kaggle Healthcare Stroke Data. Vous pouvez explorer ces informations et utiliser différents paramètres pour filtrer les patients selon vos besoins.'
)

st.write('## Filtrer les données')
options = {
    'gender': {
        None: 'Aucun filtre',
        'male': 'Homme',
        'female': 'Femme',
        'other': 'Autre',
    },
    'stroke': {0: 'non', 1: 'oui'},
}
col1, col2, col3 = st.columns(3)
gender = col1.selectbox(
    'Genre',
    [i for i in options.get('gender', {})],
    accept_new_options=False,
    format_func=lambda x: options.get('gender', {}).get(x),
)
stroke = col2.segmented_control(
    'Patients ayant eu un AVC',
    [i for i in options.get('stroke', {})],
    width='stretch',
    format_func=lambda x: options.get('stroke', {}).get(x),
)
max_age = col3.number_input('Age maximum (0 pour désactiver)', step=1, min_value=0)

st.write('## Affichage du dataframe')

st.dataframe(fetch_data(gender, stroke, max_age))
