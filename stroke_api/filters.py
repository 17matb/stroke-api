from typing import Literal
import pandas as pd
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Chargement des données (une fois)
stroke_data = pd.read_parquet('./data/data.parquet')

@app.get('/patients/')
def filter_patient(gender: Literal['male', 'female', 'other'] = None, stroke: Literal[0,1] = None, max_age: float = None) -> list[dict]:
    df = stroke_data.copy()
    if gender is not None:
        df = df.loc[df['gender'] == gender]
    if stroke is not None:
        df = df.loc[df['stroke'] == stroke]
    if max_age != 0 and max_age is not None:
        df = df.loc[df['age'] <= max_age]

    result = df.to_dict('records')
    return result

@app.get('/patients/{patient_id}')
def read_patient(patient_id):
    return {'patient_id': patient_id}

def filter_patient_by_id(patient_id):
    df = stroke_data.copy()
    df = df.loc[df['id'] == patient_id]
    if df.empty:
        raise HTTPException(404, 'Patient ID not found')
    else:
        return df.to_dict('records')

# Tester l'app avec :
# poetry run fastapi dev stroke_api/main.py
# http://127.0.0.1:8000/docs : utiliser la fonctionnalité Try it out pour tester les routes

# Ajout des fonctions de filtrage des données cf notebook 1
# Ensuite faire appel à ces fonctions dans le fichier api.py où sont définies les routes.

# Ajouter les fonctions de filtrage pour les autres routes.

