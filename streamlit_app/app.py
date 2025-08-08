import streamlit as st

st.write("""
# Projet de Visualisation et d’Exposition des Données Patients

Bienvenus sur notre plateforme de visualisation des données médicales. Ce projet a été conçu en vue de deux objectifs essentiels de gestion et d’exploitation des données de santé :

---

## Mise à disposition des données via une API REST

C’est dans ce cadre d’interopérabilité et de collaboration que nous avons développé une API REST s’appuyant sur **FastAPI**.  
Son objectif consiste bien sûr à exposer les données patients, mais d’une manière **sécurisée**, **normalisée** et **facilitant les accès** :

- **Médecins** : pour accéder à l’information clinique qui est la plus essentielle.
- **Équipes Data Science** : pour permettre ensuite d’effectuer de l’analyse ou de construire des modèles prédictifs.
- **Cellules d’études et de recherche de données** : pour exploiter les données dans le cadre d’une étude de projet scientifique ou médical.

---

## Visualisation des données avec Streamlit

Pour répondre à la question de la diffusion des données, nous avons mis en place un **dashboard interactif développé dans Streamlit**.  
L’objectif est d’offrir une interface **intuitive** et **accessible**, permettant :

- Un rendu **clair et dynamique** des données clés.
- Une **exploration interactive** des indicateurs de santé.
- Un accès à l’information **facilité pour les professionnels de santé**, sans avoir à être technicien.ne aguerri.e.

---

Ce projet répond à une volonté pérenne d’améliorer l’accès à l’information médicale,  
en préfigurant un **meilleur travail en équipe**, en contribuant à la **compréhension des données**,  
et donc en facilitant la **prise en charge des patients**.
         
Bonne visite !

**Matthis "Crackito" & Thibaud "Thorongil"**
""")
