import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Titre de la page
st.title("📊 Statistiques Générales")

# Appel API à la route /stats/
API_URL = "http://localhost:8000/stats/"

# Séparateur visuel
st.markdown("---")

# Bloc try/except pour gérer l’appel à l’API
try:
    response = requests.get(API_URL)
    response.raise_for_status()  # Vérification erreur HTTP
    stats = response.json()

    # subheader pour mettre un format texte "en tête"
    st.subheader("🧮 Indicateurs clés")

    # Affichage sous forme de colonnes (mise en page)
    col1, col2, col3 = st.columns(3)
    col1.metric("​🧾 Total Patients", stats['total_patients'])
    col2.metric("🎂 Âge moyen", f"{stats['average_age']} ans")
    col3.metric("🧠 Taux d’AVC", f"{stats['stroke_rate'] * 100:.1f}%")

    # Séparateur visuel
    st.markdown("---")

    # Titre de la section suivante
    st.subheader("👥 Répartition par genre (%)")

    # Récupération des données brutes
    original_gender_data = stats['gender_rate']  # Dictionnaire : {male: %, female: %, other: %}

    # Dictionnaire de renommage des étiquettes vers le français
    rename_map = {
        "male": "Homme",
        "female": "Femme",
        "other": "Autre"
    }

    # Transformation des clés du dictionnaire
    gender_data = {rename_map.get(gender, gender): rate for gender, rate in original_gender_data.items()}


    # Affichage des genres renommés sous forme de texte (Markdown)
    for gender, rate in gender_data.items():
        st.write(f"- **{gender}** : {rate:.2f}%")


    # Création du DataFrame avec un ordre personnalisé
    order = ["Femme", "Homme", "Autre"]  # Ordre voulu
    gender_df = pd.DataFrame({
        "Genre": pd.Categorical(list(gender_data.keys()), categories=order, ordered=True),
        "Répartition (%)": list(gender_data.values())
    }).sort_values("Genre")


    # Affichage du graphique en barres avec Streamlit
    # Ici on précise qu'on veut "Genre" comme index du graphique
    st.bar_chart(gender_df.set_index("Genre"), color=["#6A0853CC"])

# Message d'erreur si l'API n'est pas dispo ou contient une erreur
except requests.exceptions.RequestException as e:
    st.error(f"Erreur lors de l'appel à l'API : {e}")
